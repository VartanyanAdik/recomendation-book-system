import random as random
import string
import psycopg2 as pg2


def selection_genre():
    conn = pg2.connect(dbname='library', user='postgres', password='eimml55555', host='127.0.0.7')
    cur = conn.cursor()

    genres = ["Action and adventure", "Detective", "Sci-fi", "Historical fiction", "Dystopia", "Fantasy",
                "Romance novel", "Short stories", "Western", "Horror", "Classic", "Folklore", "Fairy tale",
                "Fan fiction", "Graphic novel", "Biography", "Essay", "Memoir", "Textbook", "True crime",
                "Cookbook", "Dictionary", "Handbook", "Self-help manual", "Dictionary", "Sciense", "Romance"]

    for i in range(0, 1000):
        books_genre = (random.choice(genres)) + ""
        query='INSERT INTO book_genre(genre) VALUES (%s)'
        cur.execute(query, (books_genre,))
        conn.commit()


selection_genre()
