#!/usr/bin/node
const n = parseInt(process.argv[2]);
function factorial (n) {
  if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
if (!process.argv[2] || !Number.isInteger(n)) {
  console.log('1');
} else if (Number.isInteger(n)) {
  console.log(factorial(n));
}
