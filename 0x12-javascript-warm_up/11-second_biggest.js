#!/usr/bin/node
let i = 0;
let j = 0;
let maxN = 0;
let secondMax = 0;
if (process.argv.length < 2) {
  console.log(0);
} else {
  while (i <= process.argv.length) {
    if (parseInt(process.argv[i]) > maxN) {
      maxN = parseInt(process.argv[i]);
    }
    i++;
  }
  while (j <= process.argv.length) {
    if (parseInt(process.argv[j]) < maxN && parseInt(process.argv[j]) > secondMax) {
      secondMax = parseInt(process.argv[j]);
    }
    j++;
  }
}
console.log(secondMax);
