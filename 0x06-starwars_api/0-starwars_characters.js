#!/usr/bin/node

const request = require('request');

if (process.argv.length < 3) {
  console.log('Usage: ./0-starwars_characters movieId');
  process.exit(1);
}

const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

/**
 * Wraps a request in a Promise
 *
 * @param {string} url The url to request
 * @returns {Promise}
 */
function doRequest (url) {
  return new Promise(function (resolve, reject) {
    request(url, function (error, response, body) {
      if (!error && response.statusCode === 200) {
        resolve(body);
      } else {
        reject(error);
      }
    });
  });
}

request(url, async function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const movie = JSON.parse(body);
    for (const charUrl of movie.characters) {
      try {
        const res = await doRequest(charUrl);
        const person = JSON.parse(res);
        console.log(person.name);
      } catch (error) {
        console.log(error);
      }
    }
  }
});
