const CanvasModel = (() => {
  const CELL_W = 1280;
  const CELL_H = 800;
  const PAGE_W = 1200;
  const PAGE_H = 675;
  const PAGE_X = (CELL_W - PAGE_W) / 2;
  const PAGE_Y = (CELL_H - PAGE_H) / 2;
  const centerCol = size => 1.5 - size / 2;

  const parents = {prepare:'input',decide:'input',verify:'input',data:'decide',business:'decide',engineering:'decide',sample:'data'};
  function survivingParent(id, scene) {
    const live = new Set(scene.nodes.map(node => node.id));
    let ancestor = parents[id];
    while (ancestor && !live.has(ancestor)) ancestor = parents[ancestor];
    return ancestor || 'input';
  }

  const pinchSize = (start, delta) => Math.max(1, Math.min(3, start * Math.exp(delta * .006)));

  // shortcut: wheel events lack finger-up; use an idle gap until native gesture phases are available.
  const READING_IDLE = 260;
  function readingWheel(previous, {id, delta, top, max, time}) {
    const recent = previous && time - previous.time < READING_IDLE;
    const direction = Math.sign(delta);
    if (recent && previous.locked) return {...previous, time, action:'hold'};
    const canRead = direction < 0 ? top > 1 : top < max - 1;
    const action = canRead ? 'read' : recent ? 'hold' : 'pan';
    return {id, time, direction, action, locked:action === 'pan'};
  }

  function projection(width, height, camera) {
    const fill = Math.max(0, Math.min(1, 2 - camera.size));
    const overview = Math.max(120, Math.min(width - 32, (height - 28) * CELL_W / CELL_H));
    const scale = (overview / CELL_W * (1 - fill) + width / PAGE_W * fill) / camera.size;
    const cellHeight = CELL_H * (1 - fill) + (height / (scale * camera.size) + 2 * PAGE_Y) * fill;
    return {
      scale, cellHeight, pageHeight: cellHeight - 2 * PAGE_Y,
      x: width / 2 - (camera.x + CELL_W * camera.size / 2) * scale,
      y: height / 2 - (camera.y / CELL_H + camera.size / 2) * cellHeight * scale,
    };
  }

  function zoomAnchor(camera, scene, width, height, selected) {
    const {cellHeight} = projection(width, height, camera);
    const col = camera.x / CELL_W + camera.size / 2;
    const row = camera.y / CELL_H + camera.size / 2;
    const distance = node => Math.hypot((node.col + .5 - col) * CELL_W, (node.row + .5 - row) * cellHeight);
    const preferred = scene.nodes.find(node => node.id === selected) || scene.nodes[0];
    return scene.nodes.reduce((closest, node) => distance(node) < distance(closest) - 1e-7 ? node : closest, preferred);
  }

  function zoomView(node, size, scene) {
    return snapView({col: node.col + .5 - size / 2, row: node.row + .5 - size / 2, size}, scene);
  }

  function zoomCamera(camera, size) {
    return {
      x: camera.x + (camera.size - size) * CELL_W / 2,
      y: camera.y + (camera.size - size) * CELL_H / 2,
      size,
    };
  }

  function layout({ steps = false, perspectives = false, evidence = false } = {}) {
    const nodes = [{ id: 'input', col: 1, row: 0 }];
    const edges = [];
    if (!steps) {
      nodes.push({ id: 'output', col: 1, row: 1 });
      edges.push({ from: 'input', to: 'output', kind: 'main' });
    } else {
      nodes.push({ id: 'prepare', col: 1, row: 1 }, { id: 'decide', col: 1, row: 2 });
      let nextRow = 3;
      if (perspectives) {
        ['data', 'business', 'engineering'].forEach((id, col) => {
          nodes.push({ id, col, row: 3, lane: id });
          edges.push({ from: 'decide', to: id, kind: 'perspective' });
        });
        nextRow += 1;
        if (evidence) {
          nodes.push({ id: 'sample', col: 0, row: 4, lane: 'data' });
          edges.push({ from: 'data', to: 'sample', kind: 'detail' });
          nextRow += 1;
        }
      }
      nodes.push({ id: 'verify', col: 1, row: nextRow }, { id: 'output', col: 1, row: nextRow + 1 });
      const main = ['input', 'prepare', 'decide', 'verify', 'output'];
      main.slice(1).forEach((id, index) => edges.push({ from: main[index], to: id, kind: 'main' }));
    }
    return {
      nodes,
      edges,
      maxCol: Math.max(...nodes.map(node => node.col)),
      maxRow: Math.max(...nodes.map(node => node.row)),
      hasBranches: nodes.some(node => node.lane),
    };
  }

  function clampView({ col, row, size }, scene) {
    if (![1, 2, 3].includes(size)) throw new RangeError('View size must be 1, 2, or 3.');
    return {
      col: scene.hasBranches ? Math.max(.5 - size / 2, Math.min(col, 2.5 - size / 2)) : centerCol(size),
      row: Math.max(0, Math.min(row, Math.max(0, scene.maxRow - size + 1))),
      size,
    };
  }

  function viewForNode(id, size, scene, current) {
    const node = scene.nodes.find(candidate => candidate.id === id);
    if (!node) throw new Error(`Unknown node: ${id}`);
    let col = centerCol(size);
    if (node.lane) col = size === 1 ? node.col : size === 2 ? (node.col === 0 ? 0 : node.col === 2 ? 1 : .5) : 0;
    const view = clampView({ col, row: Math.round(current?.row ?? node.row), size }, scene);
    if (node.row < view.row) view.row = node.row;
    else if (node.row + 1 > view.row + size) view.row = node.row - size + 1;
    return snapView(view, scene);
  }

  function horizontalStops(view, scene) {
    const hasVisibleBranches = scene.nodes.some(node => node.lane && node.row >= view.row && node.row < view.row + view.size);
    return hasVisibleBranches ? view.size === 1 ? [0, 1, 2] : view.size === 2 ? [-.5, 0, .5, 1, 1.5] : [-1, 0, 1] : [centerCol(view.size)];
  }

  function snapView({ col, row, size }, scene) {
    const view = clampView({ col, row: Math.round(row), size }, scene);
    const stops = horizontalStops(view, scene);
    view.col = stops.reduce((closest, candidate) => Math.abs(candidate - view.col) < Math.abs(closest - view.col) ? candidate : closest);
    return view;
  }

  function nextView(view, dc, dr, scene) {
    const next = snapView({ ...view, row: view.row + dr }, scene);
    if (dc) {
      const stops = horizontalStops(next, scene);
      const index = stops.indexOf(next.col);
      next.col = stops[Math.max(0, Math.min(stops.length - 1, index + Math.sign(dc)))];
    }
    return next;
  }

  return { readingWheel, READING_IDLE, zoomAnchor, zoomView, zoomCamera, pinchSize, projection, parents, survivingParent, CELL_W, CELL_H, PAGE_W, PAGE_H, PAGE_X, PAGE_Y, centerCol, layout, clampView, viewForNode, snapView, nextView, horizontalStops };
})();

if (typeof module !== 'undefined') module.exports = CanvasModel;
