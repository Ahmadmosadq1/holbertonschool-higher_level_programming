#!/usr/bin/node
//  importing argv from process libaray
const { argv } = require('node:process');
if (argv.length > 3) {
  console.log('Arguments found');
} else if (argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
