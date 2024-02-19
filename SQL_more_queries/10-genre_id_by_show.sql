-- This query selects the title of TV shows and their associated genre IDs from the tables tv_shows and tv_show_genres.
-- It joins the tables based on the relationship between tv_shows.id and tv_show_genres.tv_show_id.
-- Results are ordered alphabetically by the title of the TV show and then by the genre ID.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
