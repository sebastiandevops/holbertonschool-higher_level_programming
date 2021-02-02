#!/usr/bin/node
if (!process.argv[2] || !Number.isInteger(parseInt(process.argv[2]))) {
  console.log('Not a number');
} else if (Number.isInteger(process.argv[2])) {
  console.log('My number: ' + process.argv[2]);
} else {
  console.log('My number: ' + parseInt(process.argv[2]));
}
