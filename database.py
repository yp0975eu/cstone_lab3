import sqlite3
import logging


class DB:
    database_name = "lab3.db"

    def __init__(self):
        self.connection = sqlite3.connect(self.database_name)

        self.cursor = self.connection.cursor()

    def create_tables(self):
        try:
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS chainsaw_records
                (name TEXT NOT NULL,
                 country TEXT NOT NULL,
                 catches INT NOT NULL
                 );''')
            self.connection.commit()

            logging.info("Database created")

        except sqlite3.Error as er:
            print(er)

    def get_all(self):
        query = '''SELECT * FROM chainsaw_records'''
        try:
            self.cursor.execute(query)

            return self.cursor.fetchall()

        except sqlite3.Error as er:
            print('Select Error', er)

    def close_connection(self):

        self.connection.close()

    # data must be a tuple

    def insert(self, data: tuple):

        query = '''INSERT INTO chainsaw_records VALUES(?, ?, ?)'''

        try:

            self.cursor.execute(query, data)

            self.connection.commit()

        except sqlite3.Error as er:

            print("insert error", er)

