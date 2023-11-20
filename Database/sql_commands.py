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
        self.connection.execute(sql_queries.CREATE_BAN_USER_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_USER_DATA_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_LIKE_TABLE_QUERY)
        self.connection.commit()

    def insert_sql_users(self, telegram_id, username, firstname, lastname):
        self.cursor.execute(
            sql_queries.INSERT_USER_QUERY,
            (None, telegram_id, username, firstname, lastname)
        )
        self.connection.commit()

    def insert_sql_ban_user(self, telegram_id):
        self.cursor.execute(
            sql_queries.INSERT_BAN_USER_QUERY,
            (None, telegram_id, 1)
        )
        self.connection.commit()

    def insert_sql_callback(self, telegram_id, answer):
        self.cursor.execute(
            sql_queries.INSERT_CALLBACK_QUERY, (None, telegram_id, answer)
        )
        self.connection.commit()

    def select_sql_ban_user(self, telegram_id):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "telegram_id": row[1],
            "count": row[2],
        }
        return self.cursor.execute(
            sql_queries.SELECT_BAN_USER_QUERY,
            (telegram_id,)
        ).fetchone()

    def update_sql_ban_user_count(self, telegram_id):
        self.cursor.execute(
            sql_queries.UPDATE_BAN_USER_COUNT_QUERY,
            (telegram_id,)
        )
        self.connection.commit()

    def insert_sql_user_data_registration(self, telegram_id, nickname, age, gender, location, bio, photo):
        self.cursor.execute(sql_queries.INSERT_USER_DATA_QUERY,
                            (None, telegram_id, nickname, age, gender, location, bio, photo,)
                            )
        self.connection.commit()

    def insert_sql_like(self, owner, liker):
        self.cursor.execute(
            sql_queries.INSERT_LIKE_FORM_QUERY,
            (None, owner, liker)
        )
        self.connection.commit()

    def sql_select_one_user_data(self, tg_id):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "telegram_id": row[1],
            "nickname": row[2],
            "age": row[3],
            "gender": row[4],
            "location": row[5],
            "bio": row[6],
            "photo": row[7],
        }
        return self.cursor.execute(
            sql_queries.SELECT_ONE_USER_DATA, (tg_id,)
        ).fetchone()

    def select_all_user_data(self, tg_id):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "telegram_id": row[1],
            "nickname": row[2],
            "age": row[3],
            "gender": row[4],
            "location": row[5],
            "bio": row[6],
            "photo": row[7],
        }
        return self.cursor.execute(
            sql_queries.SELECT_ALL_USER_DATA,
            (tg_id,)
        ).fetchall()

    def filter_data(self, tg_id):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "telegram_id": row[1],
            "nickname": row[2],
            "age": row[3],
            "gender": row[4],
            "location": row[5],
            "bio": row[6],
            "photo": row[7],
        }
        return self.cursor.execute(
            sql_queries.FILTER_DATA_LIKE, (tg_id, tg_id,)
        ).fetchall()
