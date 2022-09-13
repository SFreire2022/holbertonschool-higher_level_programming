#!/usr/bin/node
const axios = require('axios').default;
const url = process.argv[2];

axios.get(url).then((resp) => {
  const tasks = resp.data;
  const comp = {};
  for (const task in tasks) {
    if (isNaN(comp[tasks[task].userId]) && tasks[task].completed) {
      comp[tasks[task].userId] = 0;
    }
    if (tasks[task].completed) {
      comp[tasks[task].userId] += 1;
    }
  }
  console.log(comp);
}).catch((error) => {
  console.log(error);
});
