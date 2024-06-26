#!/usr/bin/node

const request = require("request");
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(
      `Failed to fetch movie details. Status code: ${response.statusCode}`,
    );
    return;
  }

  const movieData = JSON.parse(body);
  console.log(movieData.title);
});
