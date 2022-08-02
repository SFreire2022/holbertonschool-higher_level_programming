#!/usr/bin/node
const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);
function add (a, b) {
  const res = a + b;
  console.log(res);
}

add(a, b);
