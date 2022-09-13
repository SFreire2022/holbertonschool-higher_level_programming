#!/usr/bin/node
const axios = require('axios').default;
const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;

axios.get(url).then((resp) => {
  for (const character in resp.data.characters) {
    axios.get(resp.data.characters[character]).then((resp2) => {
      console.log(resp2.data.name);
    });
  }
}).catch((error) => {
  console.log(error);
});
