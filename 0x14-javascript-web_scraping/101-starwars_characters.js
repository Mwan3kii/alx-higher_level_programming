#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
request(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const movieData = JSON.parse(body);
  const charUrls = movieData.characters;
  const charNames = (urls, index = 0) => {
    if (index >= urls.length) {
      return;
    }
    request(urls[index], (charErr, charResp, charBody) => {
      if (charErr) {
        console.error(charErr);
        return;
      }
      const charData = JSON.parse(charBody);
      console.log(charData.name);
      CharNames(urls, index + 1);
    });
  };
  CharNames(charUrls);
});
