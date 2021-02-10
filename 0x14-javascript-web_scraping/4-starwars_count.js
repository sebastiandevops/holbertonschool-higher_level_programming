#!/usr/bin/node
'use strict';
const request = require('request');
request(process.argv[2], { json: true }, function (err, response, body) {
  if (err) console.log(err); else {
    if (response.statusCode === 200) {
      let count = 0;
      body.results.forEach(film => {
        film.characters.forEach(char => {
          if (char.search('18') >= 0) count++;
        });
      });
      console.log(count);
    }
  }
});
