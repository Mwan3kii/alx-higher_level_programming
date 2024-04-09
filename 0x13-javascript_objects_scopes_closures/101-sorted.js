#!/usr/bin/node
const { dict } = require('./101-data');
const sortedDict = {};

for (const userId in dict) {
  const occurr = dict[userId];
  if (!sortedDict[occurr]) {
    sortedDict[occurr] = [];
  }
  sortedDict[occurr].push(userId);
}
console.log(sortedDict);
