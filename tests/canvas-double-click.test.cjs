const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const source = fs.readFileSync(`${__dirname}/../plugins/html-briefing/skills/html-briefing/assets/flow-canvas/presentation.template.html`, 'utf8');
const handlerSource = source.match(/\$\('blocks'\)\.addEventListener\('dblclick',[\s\S]*?\n\}\);/)[0];
let handler, entered = [], focusCount = 0, prevented = 0;
const state = {view: {size: 3}};
vm.runInNewContext(handlerSource, {
  state, focusNode: id => entered.push(id),
  $: id => id === 'blocks' ? {addEventListener: (_, fn) => handler = fn} : {focus: () => focusCount++},
});
const block = {dataset: {id: 'engineering'}, inert: false, hidden: false};
function doubleClick(interactive = false, target = block) {
  handler({target: {closest: selector => selector === '.block' ? target : interactive}, preventDefault: () => prevented++});
}
doubleClick();
assert.deepEqual(entered, ['engineering']);
assert.equal(focusCount, 1);
assert.equal(prevented, 1);
doubleClick(true);
doubleClick(false, null);
doubleClick(false, {...block, inert: true});
doubleClick(false, {...block, hidden: true});
state.view.size = 1;
doubleClick();
assert.deepEqual(entered, ['engineering']);
assert.equal(prevented, 1);
console.log('Double-click focus and interaction guards passed.');
