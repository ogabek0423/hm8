import multiprocessing
import time
from datetime import datetime
from base import Database

def write_to_file(file_path, data):
    with open(file_path, 'a') as file:
        time.sleep(3)
        file.write(data + "\n")
        print(f"Data written to {file_path}")

def insert_data(table, query):
    time.sleep(3)
    print(table, Database.connect(query, "insert"))

def select_date(table, query):
    time.sleep(3)
    print("\n")
    print(f"{table}: {Database.connect(query, "select")}\n")

def read_and_write(table1, table2):
    query = f"""SELECT * FROM {table1}"""
    data_table1 = Database.connect(query, "select")
    for i in data_table1:
        insert_query = f"""INSERT INTO {table2}(title, price) VALUES('{i[1]}', {i[2]})"""
        process1 = multiprocessing.Process(target=insert_data, args=(table2, insert_query))
        process1.start()
        process1.join()


def main():
    table1 = "film"
    table2 = "filmclone"
    process1 = multiprocessing.Process(target=read_and_write, args=(table1, table2))
    process1.start()
    process1.join()



if __name__ == "__main__":
    print(datetime.now().time())
    main()
    print(datetime.now().time())

