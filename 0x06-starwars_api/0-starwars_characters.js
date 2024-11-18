#!/usr/bin/node

import fetch from 'node-fetch';

const movie = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${movie}`;

fetch(url)
  .then(res => res.json())
  .then(data => {
    // Collect promises to fetch character data
    const characterPromises = data.characters.map(i => 
      fetch(i)
        .then(resp => resp.json())
        .then(charc => charc.name)
        .catch(error => console.error(error))
    );

    // Wait for all promises to resolve and log character names in order
    return Promise.all(characterPromises);
  })
  .then(characterNames => {
    characterNames.forEach(name => console.log(name));
  })
  .catch(error => console.error(error));
