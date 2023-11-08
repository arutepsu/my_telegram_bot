import sqlite3

from Database import sql_queries


class Database:
    def __init__(self):
        self.connection = sqlite3.connect("db.sqlite3")
        self.cursor = self.connection.cursor()

    def create_sql_tables(self):
        if self.connection:
            print("DB connected successfully")

        self.connection.execute(sql_queries.CREATE_USER_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_CALLBACK_QUERY)

    def insert_sql_users(self, telegram_id, username, firstname, lastname):
        self.cursor.execute(
            sql_queries.INSERT_USER_QUERY,
            (None, telegram_id, username, firstname, lastname)
        )
        self.connection.commit()

    def insert_sql_callback(self, telegram_id, answer):
        self.cursor.execute(
            sql_queries.INSERT_CALLBACK_QUERY, (None, telegram_id, answer)
        )
        self.connection.commit()
