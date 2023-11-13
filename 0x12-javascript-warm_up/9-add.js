#!/usr/bin/node

const add = (a, b) => {
  return a + b;
};

const arg1 = parseInt(process.argv[2]);
const arg2 = parseInt(process.argv[3]);

if (!isNaN(arg1) && !isNaN(arg2)) {
  console.log(add(arg1, arg2));
} else {
  // Print an error message
  console.log('Invalid input. Please provide two integers.');
}
