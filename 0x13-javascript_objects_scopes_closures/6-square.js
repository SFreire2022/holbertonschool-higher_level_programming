#!/usr/bin/node
const OldSquare = require('./5-square');

module.exports = class Square extends OldSquare {
  charPrint (c) {
    const character = !c ? 'X' : c;
    let i = this.height;
    for (; i > 0; i--) {
      console.log(character.repeat(this.width));
    }
  }
};
