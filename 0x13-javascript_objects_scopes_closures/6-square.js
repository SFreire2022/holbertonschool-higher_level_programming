#!/usr/bin/node
const OldSquare = require('./5-square');

module.exports = class Square extends OldSquare {
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
