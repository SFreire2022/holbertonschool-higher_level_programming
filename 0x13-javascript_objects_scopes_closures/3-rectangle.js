#!/usr/bin/node
'use strict';
module.exports = class Rectangle {
  constructor (w, h) {
    if (w >= 1 && h >= 1) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i = this.height;
    for (; i > 0; i--) {
      console.log('X'.repeat(this.width));
    }
  }
};
