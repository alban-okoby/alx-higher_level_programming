#!/usr/bin/node
const fs = require('fs');

const filePath = process.argv[2];
const contentToWrite = process.argv[3];

fs.promises.writeFile(filePath, contentToWrite, 'utf-8')
  .then(() => console.log(`Content written to ${filePath}`))
  .catch(error => console.error(`Error occurred: ${error.message}`));
