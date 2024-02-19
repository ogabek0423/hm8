import multiprocessing
from datetime import datetime
from base import Database


def select_date(table, query):
    print(f"{table}: {Database.connect(query, "select")}\n")
def main():
    table1 = 'director'
    table2 = 'film'
    # table3 = 'filmclone'

    query_select_1 = """SELECT * FROM film;"""
    query_select_2 = """SELECT * FROM director;"""
    # query_select_3 = """SELECT * FROM filmclone"""

    process1 = multiprocessing.Process(target=select_date, args=(table1, query_select_1))
    process2 = multiprocessing.Process(target=select_date, args=(table2, query_select_2))
    # process3 = multiprocessing.Process(target=select_date, args=(table3, query_select_3))


    process1.start()
    process2.start()
    # process3.start()

    process1.join()
    process2.join()
    # process3.join()



if __name__ == "__main__":
    print(datetime.now().time())
    main()
    print(datetime.now().time())
