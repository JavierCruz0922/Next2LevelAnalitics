from psycopg2 import sql

querie_extract_film_genres = sql.SQL("""
	SELECT film_id, genre_id
	FROM db_test.film_genres
""")

querie_extract_films = sql.SQL("""
	SELECT film_id, original_title, original_language, status, release_date, runtime, budget, revenue, title, tagline, overview
	FROM db_test.films
""")

querie_extract_genres = sql.SQL("""
	SELECT genre_id, genre_name
	FROM db_test.genres
""")

querie_extract_ratings_movies = sql.SQL("""
	SELECT userid, movie_id, rating, "date"
	FROM db_test.ratings_movies;
""")



