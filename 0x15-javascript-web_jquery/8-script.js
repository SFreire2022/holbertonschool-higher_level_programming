$.get('https://swapi-api.hbtn.io/api/films/?format=json', (data, textStatus) => {
  if (textStatus === 'success') {
    for (const i of data.results) {
      $('#list_movies').append(`<li>${i.title}</li>`);
    }
  }
});
