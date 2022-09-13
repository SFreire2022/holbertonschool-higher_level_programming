#!/usr/bin/node
const axios = require('axios').default;
const url = process.argv[2];
const id = '18';

axios.get(url).then((resp) => {
  let count = 0;
  for (const i in resp.data.results) {
    for (const j in resp.data.results[i].characters) {
      if (resp.data.results[i].characters[j].includes(id)) {
        ++count;
        break;
      }
    }
  }
  console.log(count);
}).catch((error) => {
  console.log(error);
});
