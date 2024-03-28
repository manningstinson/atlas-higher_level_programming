#!/usr/bin/node

const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const filePath = process.argv[3];

request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(
      `Failed to fetch webpage. Status code: ${response.statusCode}`
    );
    return;
  }

  fs.writeFile(filePath, body, { encoding: 'utf-8' }, (err) => {
    if (err) {
      console.error('Error writing file:', err);
      return;
    }
    console.log('Webpage content has been successfully stored in:', filePath);
  });
});
