#!/usr/bin/node
let a = parseInt(process.argv[2]);
if (Number.isNaN(a)) {
  console.log('Missing number of occurrences');
} else {
  for (; a > 0; a--) {
    console.log('C is fun');
  }
}
