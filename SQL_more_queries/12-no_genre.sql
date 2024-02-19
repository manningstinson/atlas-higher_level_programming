-- Script: 12-no_genre.sql
-- Description: This script lists all shows contained in hbtn_0d_tvshows without a genre linked.
-- Each record displays the title of the TV show and a NULL value for genre_id.
-- Results are sorted in ascending order by tv_shows.title and tv_show_genres.genre_id.
-- Usage: Execute this script with the database name passed as an argument of the mysql command.
-- Example: cat 12-no_genre.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
-- Author: [Your Name]
-- Date: [Date]
-- Version: 1.0

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id;
