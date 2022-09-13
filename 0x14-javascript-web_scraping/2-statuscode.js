#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (err, resp) {
  if (err == null) {
    console.log('code: ' + resp.statusCode);
  }
});
