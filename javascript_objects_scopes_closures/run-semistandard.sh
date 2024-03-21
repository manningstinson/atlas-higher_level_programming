#!/bin/bash

# Check if semistandard is installed
if ! [ -x "$(command -v semistandard)" ]; then
  echo 'Error: semistandard is not installed. Please install it using npm install -g semistandard' >&2
  exit 1
fi

# Check if a directory is provided
if [ -z "$1" ]; then
  echo 'Error: Please provide a directory.' >&2
  exit 1
fi

# Run semistandard on all JavaScript files in the provided directory
find "$1" -type f -name "*.js" -exec semistandard {} +
