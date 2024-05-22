#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];
const wAId = '18';
request(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const films = JSON.parse(body).results;
    let movieCount = 0;
    for (const filmIndex in films) {
      const filmChars = films[filmIndex].characters;
      for (const charIndex in filmChars) {
        if (filmChars[charIndex].includes(wAId)) {
          movieCount++;
        }
      }
    }
    console.log(movieCount);
  } else {
    console.log('An error occured. Status code: ' + response.statusCode);
  }
});
