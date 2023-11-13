#!/usr/bin/node

if (process.argv.length <= 2) {
  console.log('Error: Not enough arguments');
} else {
  console.log(process.argv[2] + ' is ' + process.argv[3]);
}
