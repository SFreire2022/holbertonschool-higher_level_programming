#!/usr/bin/node
function factorial (n) {
  if (n === 0) {
    return 1;
  }
  return n * factorial(n - 1);
}

const n = parseInt(process.argv[2]);
if (Number.isNaN(n) || n === 0) {
  console.log('1');
} else {
  console.log(factorial(n));
}
