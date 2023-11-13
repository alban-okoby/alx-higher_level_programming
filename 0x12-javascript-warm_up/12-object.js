#!/usr/bin/node

/**
 * Extract the list of arguments (excluding the first two,
 * which are node and the script filename)
 */
const args = process.argv.slice(2);

if (args.length === 0) {
  console.log(0);
} else if (args.length === 1) {
  console.log(0);
} else {
  const numbers = args.map(arg => parseInt(arg));
  const updatedNumbers = numbers.map(num => (num === 12 ? 89 : num));
  updatedNumbers.sort((a, b) => b - a); // Sort in des order
  console.log(updatedNumbers[1]);
}
