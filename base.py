import psycopg2 as db

import os


from dotenv import load_dotenv
load_dotenv()

class Database:
    @staticmethod
    def connect(query, data_type):
        database = db.connect(
            database=os.getenv("DATABASENAME"),
            host=os.getenv("DBHOST"),
            user=os.getenv("DBUSER"),
            password=os.getenv("PASSWOORD")
        )

        cursor = database.cursor()

        cursor.execute(query)
        data = ["insert", "delete", "update", "create"]
        if data_type in data:
            database.commit()

            if data_type == "insert":
                return "inserted"

            elif data_type == "delete":
                return "deleted"

            elif data_type == "update":
                return "updated"

            elif data_type == "create":
                return "created"

        else:
            return cursor.fetchall()




