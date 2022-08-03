#!/usr/bin/node
let instance = 0;
exports.logMe = function (item) {
  return console.log(`${instance++}: ${item}`);
};
