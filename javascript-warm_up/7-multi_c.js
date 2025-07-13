#!/usr/bin/node
const sentance = ['C is fun'];
const { argv } = require('node:process');
if (isNaN(Number(argv[2]))) {
  console.log('Missing number of occurrences');
} else {
  for (let count = 0; count < Number(argv[2]); count++) {
    for (let letter = 0; letter < sentance.length; letter++) {
      console.log(sentance[letter]);
    }
  }
}
