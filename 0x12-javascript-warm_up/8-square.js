#!/usr/bin/node
let i;
let j;
let stri = '';
const size = parseInt(process.argv[2]);
if (!Number.isInteger(size)) {
  console.log('Missing size');
} else {
  for (i = 0; i < size; i++) {
    for (j = 0; j < size; j++) {
      stri += 'X';
    }
    if (i < (size - 1)) {
      stri += '\n';
    }
  }
  console.log(stri);
}
