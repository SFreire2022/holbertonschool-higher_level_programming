#!/usr/bin/node
const axios = require('axios').default;
const episode = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + episode;

axios.get(url).then(function (resp) {
  console.log(resp.data.title);
});
