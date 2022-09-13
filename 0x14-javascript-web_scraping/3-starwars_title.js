#!/usr/bin/node
const request = require('request');
const episode = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + episode;

request(url, function (err, resp, body) {
  if (err) {
    console.error('error:', err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
