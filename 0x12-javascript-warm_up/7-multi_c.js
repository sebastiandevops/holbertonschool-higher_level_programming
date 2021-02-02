#!/usr/bin/node
let i = 0;
if (!Number.isInteger(parseInt(process.argv[2]))) {
  console.log('Missing number of occurrences');
} else {
  while (i < parseInt(process.argv[2])) {
    console.log('c is fun');
    i++;
  }
}
