#!/usr/bin/node
// increments and calls a function
function addMeMaybe (number, theFunction) {
  number += 1;
  theFunction(number);
}
module.exports.addMeMaybe = addMeMaybe;
