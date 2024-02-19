import multiprocessing
import time
from datetime import datetime
from base import Database


def insert_data(table, query):
    time.sleep(3)
    print(table, Database.connect(query, "insert"))


def main():
    table1 = 'film'
    table2 = 'director'


    data_film = {"column": ('title', 'price'), "values": ('spiderman', 200)}
    data_director = {"column": ('first_name', 'last_name', 'birth_date'), "values": ('John', 'Smith', '2003-11-25')}
    query_1 = f"""INSERT INTO film(title, price) VALUES('{data_film["values"][0]}', {data_film["values"][1]})"""
    query_2 = f"""INSERT INTO director(first_name, last_name, birth_date) VALUES('{data_director["values"][0]}', '{data_director["values"][1]}', '{data_director["values"][2]}')"""


    process1 = multiprocessing.Process(target=insert_data, args=(table1, query_1))
    process2 = multiprocessing.Process(target=insert_data, args=(table2, query_2))

    process1.start()
    process2.start()

    process1.join()
    process2.join()


if __name__ == "__main__":
    print(datetime.now().time())
    main()
    print(datetime.now().time())
