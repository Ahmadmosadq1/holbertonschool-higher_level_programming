#!/usr/bin/node
const { argv } = require('node:process');
if (!argv[2]) {
  console.log(1);
} else {
  const num = Number(argv[2]);
  function factorial (num) {
    if (num === 0 || num === 1) return 1;
    return num * factorial(num - 1);
  }
  console.log(factorial(num));
}
