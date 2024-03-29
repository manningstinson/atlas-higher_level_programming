/* global $ */

$(document).ready(function () {
	$.get("https://swapi-api.hbtn.io/api/films/?format=json", function (data) {
		data.results.forEach(function (movie) {
			$("<li>").text(movie.title).appendTo("#list_movies");
		});
	});
});
