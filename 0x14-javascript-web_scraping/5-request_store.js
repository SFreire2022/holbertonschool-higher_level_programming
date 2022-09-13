#!/usr/bin/node
const axios = require('axios').default;
const url = process.argv[2];
const filename = process.argv[3];
const fs = require('fs');

axios.get(url).then((resp) => {
  fs.writeFile(filename, resp.data, 'utf8', function (err) {
    if (err) {
      console.log(err);
    }
  });
}).catch((error) => {
  console.log(error);
});
