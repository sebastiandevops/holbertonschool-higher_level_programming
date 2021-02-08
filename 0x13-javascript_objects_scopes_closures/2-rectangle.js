#!/usr/bin/node
'use strict';
module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
      this.w = undefined;
      this.h = undefined;
    } else {
      this.width = w;
      this.height = h;
    }
  }
};
