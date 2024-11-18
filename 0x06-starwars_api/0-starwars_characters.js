#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
if (!movieId) {
  console.error('Please provide a Movie ID as an argument.');
  process.exit(1);
}

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Failed to fetch movie. Status code: ${response.statusCode}`);
    return;
  }

  try {
    const data = JSON.parse(body);
    const characters = data.characters;

    // Fetch and print each character in order
    const fetchCharacter = (index) => {
      if (index >= characters.length) return;

      request(characters[index], (charError, charResponse, charBody) => {
        if (charError) {
          console.error('Error:', charError);
          return;
        }

        if (charResponse.statusCode === 200) {
          const characterData = JSON.parse(charBody);
          console.log(characterData.name);
          fetchCharacter(index + 1); // Fetch the next character
        } else {
          console.error(`Failed to fetch character. Status code: ${charResponse.statusCode}`);
        }
      });
    };

    fetchCharacter(0); // Start fetching characters
  } catch (parseError) {
    console.error('Error parsing JSON:', parseError);
  }
});
