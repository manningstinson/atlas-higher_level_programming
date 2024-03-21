#!/usr/bin/node

const x = parseInt(process.argv[2]);

if (isNaN(x) || x < 1) {
  // Do nothing when input is invalid
} else {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
