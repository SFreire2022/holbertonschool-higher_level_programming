#!/usr/bin/node
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (typeof (c) === 'undefined') {
      c = 'X';
    }
    // c = !c ? 'X' : c; requirment no meet but works fine
    let i = this.height;
    for (; i > 0; i--) {
      console.log(c.repeat(this.width));
    }
  }
};
