#!/usr/bin/node
// Javascript program to find second largest
// element in an array
const arr = process.argv.slice(2).map((x) => {
  return parseInt(x);
});
if (Number.isNaN(arr) || arr === 0) {
  console.log('0');
} else {
  const ArrSize = arr.length;
  print2largest(arr, ArrSize);
}

// Function to print the second largest elements
function print2largest (arr, ArrSize) {
  let i;
  let second;
  let largest = second = -2454635434;

  // There should be atleast two elements
  if (ArrSize < 2) {
    console.log('0');
    return;
  }
  // finding the largest element
  for (i = 0; i < ArrSize; i++) {
    if (arr[i] > largest) {
      second = largest;
      largest = arr[i];
    } else if (arr[i] !== largest && arr[i] > second) {
      second = arr[i];
    }
  }

  if (second === -2454635434) {
    console.log('0');
  } else {
    console.log(second);
  }
}
