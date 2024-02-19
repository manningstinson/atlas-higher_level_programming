-- Script: 13-count_shows_by_genre.sql
-- Description: This script lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
-- Each record displays the TV show genre and the number of shows linked to that genre.
-- Genres without any linked shows are not displayed.
-- Results are sorted in descending order by the number of shows linked.
-- Usage: Execute this script with the database name passed as an argument of the mysql command.
-- Example: cat 13-count_shows_by_genre.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
-- Author: [Your Name]
-- Date: [Date]
-- Version: 1.0

SELECT tv_genres.genre AS genre, COUNT(tv_shows.id) AS number_of_shows
FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
GROUP BY tv_genres.genre
ORDER BY number_of_shows DESC;
