#!/usr/bin/node
exports.esrever = function (list) {
  var rev = [];
  for (var i = list.length - 1; i >= 0; i--) {
    rev.push(list[i]);
  }
  return rev;
};
