#!/usr/bin/node
const { argv } = require('node:process');
if (argv[3]) {
  console.log(argv[2] + ' is ' + argv[3]);
} else if (!argv[3] && argv[2]) {
  console.log(argv[2] + ' is undefined');
} else {
  console.log('undefined is undefined');
}
