#!/usr/bin/node

// Function that returns the number of occurrences of a specific element in a list
exports.nbOccurrences = function (list, searchElement) {
  let count = 0;
  for (const element of list) {
    if (element === searchElement) {
      count++;
    }
  }
  return count;
};
