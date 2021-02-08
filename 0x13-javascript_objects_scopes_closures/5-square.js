#!/usr/bin/node
'use strict';
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super();
    this.size = size;
    super.width = size;
    super.height = size;
  }
};
