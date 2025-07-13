#!/usr/bin/node
const { argv } = require('node:process');
if (isNaN(Number(argv[2]))) {
  console.log('Missing size');
}

for (let row = 0; row <= Number(argv[2]); row++) {
  for (let col = 0; col <= Number(argv[2]); col++) {
    process.stdout.write('X');
  }
  console.log();
}
