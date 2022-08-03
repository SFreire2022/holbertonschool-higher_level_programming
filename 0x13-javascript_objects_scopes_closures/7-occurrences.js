#!/usr/bin/node
// Function to return number of ocurreces for a given parameter in a given list
exports.nbOccurences = function (list, searchElement) {
  let ocurreces = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      ocurreces++;
    }
  }
  return ocurreces;
};
