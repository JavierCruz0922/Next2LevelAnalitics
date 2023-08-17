from resources_conection.data_conection import PostgreSQLConnection
import Test.queries as queries
import pandas as pd

dm_user = 'daniel_cristancho'
dm_host_name = 'next2leveldb.cqn3neunxdth.us-east-2.rds.amazonaws.com'
dm_password = '9L5uGK2Fw6mPby'
dm_db = 'postgres'


dmdb = PostgreSQLConnection(user=dm_user, password=dm_password,
                            host_name=dm_host_name, database=dm_db)
dmdb.create_connection()

def __extract(conn_name, query, params: dict = None, source=None):

	try:
		query = query.as_string(conn_name)
		data = pd.read_sql(query, conn_name.connection, params=params)
	except Exception as e:
		raise
	return data

film_genres = __extract(dmdb,queries.querie_extract_film_genres,
                       source='source.extrac_data')

films = __extract(dmdb,queries.querie_extract_films,
                        source='source.extrac_data')

genres = __extract(dmdb,queries.querie_extract_genres,
                  source='source.extrac_data')

rating_movies = __extract(dmdb,queries.querie_extract_ratings_movies,
                  source='source.extrac_data')

print('x')
dmdb.destroy_connection()