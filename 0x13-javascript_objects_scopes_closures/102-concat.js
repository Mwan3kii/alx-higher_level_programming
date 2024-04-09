#!/usr/bin/node
const fs = require('fs');
const [, , fileA, fileB, fileC] = process.argv;
const contA = fs.readFileSync(fileA, 'utf8').trim();
const contB = fs.readFileSync(fileB, 'utf8');
const concateContent = contA + '\n' + contB;
fs.writeFileSync(fileC, concateContent);
