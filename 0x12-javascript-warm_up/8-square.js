#!/usr/bin/node
let side = parseInt(process.argv[2]);
const i = side;
if (Number.isNaN(side)) {
  console.log('Missing size');
} else {
  for (; side > 0; side--) {
    console.log('X'.repeat(i));
  }
}
