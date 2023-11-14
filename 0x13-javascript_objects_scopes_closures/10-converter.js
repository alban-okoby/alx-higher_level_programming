#!/usr/bin/node

exports.converter = function (base) {
  // Use the 'this' context to access the argument passed to the function
  const convertedNumber = this.toString(base);
  console.log(convertedNumber);
};
