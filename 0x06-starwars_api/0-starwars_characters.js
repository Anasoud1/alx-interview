#!/usr/bin/node
const request = require('request');
const mainUrl = 'https://swapi-api.alx-tools.com/api/films/';

if (process.argv.length === 3) {
  request.get(mainUrl, { json: true }, (err, res, body) => {
    if (err) {
      return console.error('Request failed:', err);
    }
    if (res.statusCode !== 200) {
      return console.error('Error:', res.statusCode, body);
    }
    const characterUrls = body.results[process.argv[2] - 1].characters;
    const characterNames = characterUrls.map(
      url => new Promise((resolve, reject) => {
        request.get(url, { json: true }, (err, res, body) => {
          if (err) {
            reject(err);
          }
          resolve(body.name);
        });
      }));
    Promise.all(characterNames)
      .then(names => console.log(names.join('\n')))
      .catch(error => console.log(error));
  });
}
