#!/usr/bin/node
const { argv } = require('node:process');

if (argv.length <= 3) {
  console.log(0);
} else {
  let biggest = Number(argv[2]);
  let second = Number(argv[3]);

  if (second > biggest) {
    [biggest, second] = [second, biggest];
  }

  for (let i = 4; i < argv.length; i++) {
    const num = Number(argv[i]);
    if (num > biggest) {
      second = biggest;
      biggest = num;
    } else if (num > second) {
      second = num;
    }
  }

  console.log(second);
}
