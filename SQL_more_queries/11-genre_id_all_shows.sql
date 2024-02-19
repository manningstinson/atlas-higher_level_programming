-- Select all shows and their associated genre IDs, including NULL if a show doesn't have a genre
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
-- Left join the tv_shows table with the tv_show_genres table
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
-- Order the results by show title and genre ID in ascending order
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
