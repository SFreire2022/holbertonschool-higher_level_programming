#!/usr/bin/node
if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  // print all the arguments pased to process.argv[1]
  // const args = process.argv.slice(2);
  // args.forEach((arg) => {
  //   console.log(arg);
  // });
  console.log(process.argv[2]);
}
