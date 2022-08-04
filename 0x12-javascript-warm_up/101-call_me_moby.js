#!/usr/bin/node
exports.callMeMoby = function (x, myCallback) {
  for (; x > 0; x--) {
    myCallback();
  }
};
