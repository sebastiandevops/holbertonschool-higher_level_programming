#!/usr/bin/node
let calls = -1;
exports.logMe = function (item) {
  calls++;
  console.log(calls + ': ' + item);
};
