#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(
      `Failed to fetch movie details. Status code: ${response.statusCode}`
    );
    return;
  }

  const films = JSON.parse(body);
  let wedgeAntillesMovies = 0;

  for (const film of films) {
    if (film.characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
      wedgeAntillesMovies++;
    }
  }

  console.log(wedgeAntillesMovies);
});
