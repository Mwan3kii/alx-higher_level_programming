#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  let data;
  try {
    data = JSON.parse(body);
  } catch (parseError) {
    console.error(parseError);
    return;
  }
  const completedTasks = {};
  data.forEach(task => {
    if (task.completed) {
      if (!completedTasks[task.userId]) {
        completedTasks[task.userId] = 0;
      }
      completedTasks[task.userId]++;
    }
  });
  console.log(completedTasks);
});
