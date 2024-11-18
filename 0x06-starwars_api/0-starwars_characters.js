#!/usr/bin/node

import fetch from 'node-fetch';

const movie = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${movie}`;

fetch(url)
  .then(res => res.json())
  .then(data => {
    for (const i of data.characters) {
      fetch(i)
        .then(resp => resp.json())
        .then(charc => console.log(charc.name))
        .catch(error => console.error(error));
    }
  }
  )
  .catch(error => console.error(error));
