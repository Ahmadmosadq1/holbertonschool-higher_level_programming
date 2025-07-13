#!/usr/bin/node
function add (a, b) {
  console.log(a + b);
}
const { argv } = require('node:process');
if (!argv[3]) {
  console.log('NaN');
} else {
  const a = Number(argv[2]);
  const b = Number(argv[3]);
  add(a, b);
}
