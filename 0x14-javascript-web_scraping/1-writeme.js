#!/usr/bin/node
const fs = require('fs');
const fpath = process.argv[2];
const content = process.argv[3];
fs.writeFile(fpath, content, 'utf8', (err) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log('File has been written');
});
