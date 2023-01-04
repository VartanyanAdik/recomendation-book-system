import random as random
import string
import psycopg2 as pg2


def selection_library():
    conn = pg2.connect(dbname='library', user='postgres', password='eimml55555', host='127.0.0.7')
    cur = conn.cursor()


    author_names = ["Jack", "John", "Mark", "Dan", "Nik", "Edward", "Harry", "Oliver", "Jacob", "Robert",
                    "Cristian",
                    "Ilon", "Bil", "Andrew", "Arthur", "Alexander", "Tom", "Chad", "Anthony", "Arnold", "Alfred",
                    "Andrian",
                    "Adam", "Derek", "Eric", "Ghenry", "Gerald", "Kurt", "Kevin", "Jasper", "Mickle", "Dustin",
                    "Jan",
                    "Malcon", "Oscar", "Tyler", "Norton"]

    author_surname = ["Winston", "Jhonson", "Miller", "Keane", "Eriksen", "Hans", "Smith", "William", "Brown",
                      "Black",
                      "White", "Wilson", "Dobber", "Klinton", "Garcia", "Martinez", "Young", "Hill", "King",
                      "Perez",
                      "Thompson", "Cox", "Howward", "Ford", "Brooks", "Diaz", "Lopes", "Long", "Parker", "Phillips",
                      "Carter", "Nelson", "Anderson", "Franklin", "Harris"]

    books_name_adjective = ["Close", "Dark", "Alone", "Cold", "Common", "Complete", "Dry", "Fast", "Free", "Easy",
                            "Good",
                            "Another", "Heavy", "Bad", "Kind", "Late", "Old", "Poor", "Real", "Red", "Black",
                            "Round",
                            "Safe",
                            "Sweet", "Warm", "Slow", "Yuong", "Wooden", "Wide", "Great", "Full", "Human", "Hor",
                            "Empty", "Dry",
                            "Deep", "Big", "Huge", "Nice", "Fantastic", "Horrible", "Common"]

    books_name_nouns = ["book", "man", "girl", "car", "bird", "computer", "house", "area", "animal", "air", "city",
                        "color", "day",
                        "face", "door", "fire", "family", "fish", "road", "idea", "king", "love", "money", "list",
                        "pen", "order",
                        "killer", "plant", "rock", "ahip", "song", "singer", "state", "flag", "water", "night",
                        "day",
                        "pen", "gun",
                        "teacher", "bottle", "cake", "woman", "lady"]

    for i in range(0, 1000):
        book_name = (random.choice(books_name_adjective) + " " + random.choice(books_name_nouns))
        author = (random.choice(author_names) + " " + random.choice(author_surname))
        query='INSERT INTO library(author, book_name) VALUES((%s), (%s))'
        cur.execute(query, (author, book_name))
        conn.commit()

        


selection_library()




