import time
from datetime import datetime
from base import Database

def create():
    film = """
        CREATE TABLE film(
            film_id SERIAL PRIMARY KEY,
            title VARCHAR(20),
            price FLOAT,
            created_date TIMESTAMP DEFAULT now());
    """

    director = """
            CREATE TABLE director(
                director_id SERIAL PRIMARY KEY,
                first_name VARCHAR(20),
                last_name VARCHAR(20),
                birth_date DATE,
                created_date TIMESTAMP DEFAULT now());
        """


    filmdirector = """
        CREATE TABLE filmdirector(
            filmdirector_id SERIAL PRIMARY KEY,
            film_id INT REFERENCES film(film_id),
            director_id INT REFERENCES director(director_id))
    """

    filmclone = """
            CREATE TABLE filmclone(
                filmclone_id SERIAL PRIMARY KEY,
                title VARCHAR(20),
                price FLOAT,
                created_date TIMESTAMP DEFAULT now());
        """


    data_tables = {
        "film": film,
        "director": director,
        "filmdirector": filmdirector,
        "filmclone": filmclone
    }

    for i in data_tables:
        print(f"Database {i} + {Database.connect(data_tables[i], "create")}")


if __name__ == "__main__":
    print(datetime.now().time())
    create()
    print(datetime.now().time())


