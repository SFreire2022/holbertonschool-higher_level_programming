#!/usr/bin/node
const axios = require('axios').default;
const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;

async function getAsync () {
  try {
    const resp = await axios.get(url);
    for (const charID in resp.data.characters) {
      const respChar = await axios.get(resp.data.characters[charID]);
      console.log(respChar.data.name);
    }
  } catch (error) {
    console.log(error);
  }
}
getAsync();
