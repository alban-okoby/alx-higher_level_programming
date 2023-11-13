#!/usr/bin/node

// Define a function to increment a number and call another function
const incrementAndCall = (number, theFunction) => {
  const incrementedNumber = number + 1;
  theFunction(incrementedNumber);
};

// Eg usage
const myFunction = (value) => {
  console.log('Incremented value:', value);
};

incrementAndCall(5, myFunction);
