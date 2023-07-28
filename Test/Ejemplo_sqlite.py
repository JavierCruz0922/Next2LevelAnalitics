import sqlite3
import pandas as pd

location = ('C:/Users/Laura Hijuelos/AppData/Roaming/DBeaverData/workspace6/.metadata/sample-database-sqlite-1'
                 '/Chinook.db')


def select_to_dataframe(location, select_query):
    conn = sqlite3.connect(location)
    df = pd.read_sql_query(select_query, conn)
    conn.close()

    return df


querie1 = """SELECT AlbumId, Title, ArtistId, Column1 
             FROM Album"""
querie2 = """SELECT TrackId, Name, AlbumId, MediaTypeId, GenreId, Composer, Milliseconds, Bytes, UnitPrice
             FROM Track"""

df_album = select_to_dataframe(location, querie1)
df_track = select_to_dataframe(location, querie2)

df_album_track = df_track.merge(df_album, left_on=['AlbumId'], right_on=['AlbumId'], how='left')


print('z')
