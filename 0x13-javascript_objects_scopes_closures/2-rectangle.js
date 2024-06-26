#!/usr/bin/node
// empty class Rectangle that defines a rectangle
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || isNaN(w) || isNaN(h)) {
      return ('Rectangle {}');
    }
    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
