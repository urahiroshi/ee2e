var length = 20;
var makeRand = (max) => () => Math.floor(Math.random() * max);
var toString = (Adx1, Ady1, Adx2, Ady2, Bdx1, Bdy1, Bdx2, Bdy2) => (
  `- [[${Adx1}, ${Ady1}, ${Adx2}, ${Ady2}], [${Bdx1}, ${Bdy1}, ${Bdx2}, ${Bdy2}]]`
);

var l = [];
(() => {
  const init = 100;
  const diff = 60;
  const rand = makeRand(30);
  for (let i=0; i<length; i++) {
    let v = init + i * diff;
    l.push(toString(v+rand(), 0, v+rand(), 0, v+diff+rand(), 0, v+diff+rand(), 0));
  }
})();

(() => {
  const init = 30;
  const diff = 20;
  const rand = makeRand(5);
  for (let i=0; i<length; i++) {
    let v = init + i * diff;
    l.push(toString(0, v+rand(), 0, v+rand(), 0, v+diff+rand(), 0, v+diff+rand()));
  }
})();

(() => {
  const init = -100;
  const diff = 60;
  const rand = makeRand(30);
  for (let i=0; i<length; i++) {
    let v = init - i * diff;
    l.push(toString(v-rand(), 0, v-rand(), 0, v-diff-rand(), 0, v-diff-rand(), 0));
  }
})();

(() => {
  const init = -30;
  const diff = 20;
  const rand = makeRand(5);
  for (let i=0; i<length; i++) {
    let v = init - i * diff;
    l.push(toString(0, v-rand(), 0, v-rand(), 0, v-diff-rand(), 0, v-diff-rand()));
  }
})();

console.log(l.join('\n'));
