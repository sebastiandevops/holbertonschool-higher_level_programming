#!/usr/bin/node
const number1 = parseInt(process.argv[2]);
const number2 = parseInt(process.argv[3]);
function add (a, b) {
  return a + b;
}
if (!process.argv[2] || !process.argv[3] || !Number.isInteger(number1) || !Number.isFinite(number2)) {
  console.log('NaN');
} else if (Number.isInteger(number1) && Number.isFinite(number2)) {
  console.log(add(number1, number2));
}
