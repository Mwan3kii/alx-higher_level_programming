#!/usr/bin/node
// class Square that defines a square and inherits from Rectangle
const BaseSquare = require('./5-square');

class Square extends BaseSquare {
  charPrint(c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.size; i++) {
      console.log(c.repeat(this.size));
    }
  }
}

module.exports = Square;
