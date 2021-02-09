#!/usr/bin/node
'use strict';
const Square1 = require('./5-square');

module.exports = class Square extends Square1 {
  charPrint (c) {
    if (typeof c === 'undefined') {
      let stri = '';
      for (let i = 0; i < this.width; i++) {
        for (let j = 0; j < this.height; j++) {
          stri += 'X';
        }
        if (i < (this.width - 1)) {
          stri += '\n';
        }
      }
      console.log(stri);
    } else {
      let stri = '';
      for (let i = 0; i < this.width; i++) {
        for (let j = 0; j < this.height; j++) {
          stri += String(c);
        }
        if (i < (this.width - 1)) {
          stri += '\n';
        }
      }
      console.log(stri);
    }
  }
};
