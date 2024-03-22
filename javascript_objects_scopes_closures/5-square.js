#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    // Call the constructor of the parent class with the size for both width and height
    super(size, size);
  }
}

module.exports = Square;
