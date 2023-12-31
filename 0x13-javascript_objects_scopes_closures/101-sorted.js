#!/usr/bin/node

const { dict } = require('./101-data');

// Compute a new dictionary
const occurrencesById = Object.keys(dict).reduce((newDict, userId) => {
  const occurrences = dict[userId];

  if (newDict[occurrences]) {
    newDict[occurrences].push(userId);
  } else {
    newDict[occurrences] = [userId];
  }

  return newDict;
}, {});
