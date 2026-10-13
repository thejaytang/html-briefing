const assert = require('node:assert/strict');
const {PAGE_W,PAGE_H,layout,clampView,viewForNode,snapView,nextView,centerCol,horizontalStops}=require('../plugins/html-briefing/skills/html-briefing/assets/flow-canvas/canvas-model.js');
assert.equal(PAGE_W/PAGE_H,16/9);
for(const steps of [false,true])for(const perspectives of [false,true])for(const evidence of [false,true]){
 const scene=layout({steps,perspectives,evidence}), count=!steps?2:!perspectives?5:evidence?9:8;
 assert.equal(scene.nodes.length,count);
 assert.equal(new Set(scene.nodes.map(n=>`${n.col},${n.row}`)).size,count);
 assert.ok(scene.nodes.filter(n=>!n.lane).every(n=>n.col===1),'Main pages share the center axis');
 for(const edge of scene.edges)for(const id of [edge.from,edge.to])assert.ok(scene.nodes.some(n=>n.id===id));
 for(const size of [1,2,3]){
  if(!scene.hasBranches)assert.equal(clampView({col:99,row:0,size},scene).col+size/2,1.5,'Sparse main line is viewport-centered');
  for(const node of scene.nodes){
   const v=viewForNode(node.id,size,scene,{col:99,row:99,size});
   assert.ok(v.col<=node.col&&node.col+1<=v.col+size);
   assert.ok(v.row<=node.row&&node.row+1<=v.row+size);
   assert.deepEqual(snapView(v,scene),v);
   if(!node.lane)assert.equal(v.col,centerCol(size));
  }
  for(let row=0;row<=scene.maxRow;row+=.4)for(let col=-1;col<=3;col+=.4){
   const v=snapView({col,row,size},scene);
   assert.ok(horizontalStops(v,scene).includes(v.col));
   assert.ok(Number.isInteger(v.row));
   assert.equal(v.size,size);
  }
 }
}
const expanded=layout({steps:true,perspectives:true,evidence:true});
assert.deepEqual(nextView({col:.5,row:2,size:2},1,0,expanded),{col:1,row:2,size:2});
assert.deepEqual(nextView({col:1,row:2,size:2},-1,0,expanded),{col:.5,row:2,size:2});
assert.deepEqual(nextView({col:0,row:4,size:1},0,1,expanded),{col:1,row:5,size:1},'Returning from a branch re-centers the main line');
assert.deepEqual(snapView({col:.51,row:2.49,size:2},expanded),{col:.5,row:2,size:2});
for(const size of [0,4,1.5,'2',undefined,NaN])assert.throws(()=>clampView({col:0,row:0,size},expanded),RangeError);
assert.throws(()=>viewForNode('missing',1,expanded),/Unknown node/);
console.log('Canvas model: center axis, full-page focus, 1/4/9 views, branch navigation and snap checks passed.');

const {survivingParent}=require('../plugins/html-briefing/skills/html-briefing/assets/flow-canvas/canvas-model.js');
assert.equal(survivingParent('sample',layout({steps:true,perspectives:true})),'data');
assert.equal(survivingParent('sample',layout({steps:true})),'decide');
assert.equal(survivingParent('sample',layout()),'input');
for(const id of ['data','business','engineering'])assert.equal(survivingParent(id,layout({steps:true})),'decide');
console.log('Collapse ancestry: nested pages return to the nearest surviving chapter.');
const {projection,CELL_W,CELL_H,PAGE_X,PAGE_Y}=require('../plugins/html-briefing/skills/html-briefing/assets/flow-canvas/canvas-model.js');
for(const [width,height] of [[733,623.8047],[1280,504.8047],[520,532],[1600,700]]){
 for(const col of [0,1,2])for(const row of [0,2,5]){
  const p=projection(width,height,{x:col*CELL_W,y:row*CELL_H,size:1});
  const left=p.x+(col*CELL_W+PAGE_X)*p.scale;
  const top=p.y+(row*p.cellHeight+PAGE_Y)*p.scale;
  assert.ok(Math.abs(left)<1e-8&&Math.abs(top)<1e-8,'Focused slide starts at stage origin');
  assert.ok(Math.abs(PAGE_W*p.scale-width)<1e-8,'Slide spans full width');
  assert.ok(Math.abs(p.pageHeight*p.scale-height)<1e-8,'Slide spans full height');
 }
 for(let size=1;size<=3;size+=.1){
  const p=projection(width,height,{x:centerCol(size)*CELL_W,y:2*CELL_H,size});
  assert.ok(p.scale>0&&p.pageHeight>0);
  assert.ok(Math.abs(p.x+1.5*CELL_W*p.scale-width/2)<1e-8,'Zoom preserves main center');
 }
}
console.log('Full-stage focus and continuous centered zoom: passed.');
const {pinchSize}=require('../plugins/html-briefing/skills/html-briefing/assets/flow-canvas/canvas-model.js');
assert.equal(pinchSize(2,0),2);
assert.ok(pinchSize(2,-30)<2,'Pinching outward zooms into fewer pages');
assert.ok(pinchSize(2,30)>2,'Pinching inward reveals more pages');
assert.equal(pinchSize(2,-1000),1);
assert.equal(pinchSize(2,1000),3);
for(const size of [1,2,3])assert.ok(Math.abs(pinchSize(2,Math.log(size/2)/.006)-size)<1e-9,'Wheel and native scale gestures share the same zoom mapping');
console.log('Pinch mapping, bounds and native-scale equivalence: passed.');

for(const size of [1,2,3]){
 let right={col:centerCol(size),row:2,size};
 // Include the perspective row at every zoom level.
 right.row=size===1?3:2;
 let left={...right};
 for(let step=0;step<6;step++){
  right=nextView(right,1,0,expanded);
  left=nextView(left,-1,0,expanded);
 }
 assert.equal(right.col+size/2,2.5,'Rightmost page can reach the viewport center');
 assert.equal(left.col+size/2,.5,'Leftmost page can reach the viewport center');
 assert.deepEqual(snapView(clampView({...right,col:100},expanded),expanded),right,'Wheel/drag can reach the same right endpoint');
 assert.deepEqual(snapView(clampView({...left,col:-100},expanded),expanded),left,'Wheel/drag can reach the same left endpoint');
 for(const [view,nodeCol] of [[right,2],[left,0]]){
  const p=projection(1618,1344,{x:view.col*CELL_W,y:view.row*CELL_H,size});
  assert.ok(Math.abs(p.x+(nodeCol+.5)*CELL_W*p.scale-809)<1e-8,'Edge page is geometrically centered');
 }
 assert.equal(nextView(right,0,-2,expanded).col,centerCol(size),'Main-only rows still re-center');
}
console.log('Outer perspective pages can center at 1/4/9 zoom via keys, wheel and drag bounds.');

const {zoomAnchor,zoomView,zoomCamera}=require('../plugins/html-briefing/skills/html-briefing/assets/flow-canvas/canvas-model.js');
for(const [width,height] of [[1618,1344],[733,827],[1280,720]]){
 for(const [id,col] of [['data',0],['business',1],['engineering',2]]){
  const camera={x:(col-.5)*CELL_W,y:(col===1?2.25:2)*CELL_H,size:2};
  const anchor=zoomAnchor(camera,expanded,width,height,'decide');
  assert.equal(anchor.id,id,'Zoom chooses the page at the current center, not the previous chapter');
  const one=zoomView(anchor,1,expanded);
  assert.deepEqual(one,{col,row:3,size:1},'Zooming in lands on the current perspective');
  for(const size of [2,3]){
   const out=zoomView(anchor,size,expanded);
   assert.equal(out.col+size/2,col+.5,'Zooming out retains the perspective axis');
   const next=zoomAnchor({x:out.col*CELL_W,y:out.row*CELL_H,size},expanded,width,height,id);
   assert.equal(next.id,id,'Zoom out and back in keeps the same page');
  }
  for(const size of [1,1.25,2,2.75,3]){
   const preview=zoomCamera(camera,size);
   const p=projection(width,height,preview);
   assert.ok(Math.abs(p.x+(col+.5)*CELL_W*p.scale-width/2)<1e-8,'Pinch preview retains the lateral center continuously');
  }
 }
}
const mainAnchor=zoomAnchor({x:CELL_W,y:CELL_H,size:1},expanded,1280,720,'engineering');
assert.equal(mainAnchor.id,'prepare','Main pages remain valid zoom anchors');
assert.equal(zoomView(mainAnchor,3,expanded).col,centerCol(3));
console.log('Zoom focus: left/center/right pages, stale chapter selection, continuous pinch and round trips passed.');

assert.equal(zoomAnchor({x:.5*CELL_W,y:2*CELL_H,size:2},expanded,1280,720,'decide').id,'decide','An exact distance tie keeps the current page');

const {readingWheel,READING_IDLE}=require('../plugins/html-briefing/skills/html-briefing/assets/flow-canvas/canvas-model.js');
const readEvent={id:'data',delta:80,top:200,max:1000,time:0};
let gesture=readingWheel(null,readEvent);
assert.equal(gesture.action,'read');
gesture=readingWheel(gesture,{...readEvent,top:1000,time:30});
assert.equal(gesture.action,'hold','Reaching the bottom in the same gesture does not move the canvas');
gesture=readingWheel(gesture,{...readEvent,top:1000,time:200});
assert.equal(gesture.action,'hold','Momentum remains inside the page');
gesture=readingWheel(gesture,{...readEvent,top:1000,time:200+READING_IDLE+1});
assert.equal(gesture.action,'pan','A new gesture at the bottom changes nodes');
assert.equal(gesture.direction,1);
gesture=readingWheel(gesture,{...readEvent,id:'verify',top:0,time:220+READING_IDLE});
assert.equal(gesture.action,'hold','One gesture cannot skip multiple nodes');
const reverse=readingWheel(null,{...readEvent,delta:-80,top:0,time:1000});
assert.equal(reverse.action,'pan');assert.equal(reverse.direction,-1);
const backInside=readingWheel({...readEvent,locked:false},{...readEvent,delta:-80,top:1000,time:50});
assert.equal(backInside.action,'read','Reversing from the bottom immediately reads upward');
console.log('Reading gesture: internal scroll, boundary hold, release-to-switch, reversal and inertia lock passed.');
