#!/usr/bin/node
//  importing argv from process libaray
const { argv } = require('node:process');
if (argv.length > 2) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
