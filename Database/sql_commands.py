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
        self.connection.execute(sql_queries.CREATE_REFERRAL_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_BALANCE_QUERY)
        try:
            self.connection.execute(sql_queries.ALTER_USER_TABLE_RL)
            # self.connection.execute(sql_queries.ALTER_USER_TABLE_B)
        except sqlite3.OperationalError:
            pass

        self.connection.commit()

    def insert_sql_users(self, telegram_id, username, firstname, lastname):
        self.cursor.execute(
            sql_queries.INSERT_USER_QUERY,
            (None, telegram_id, username, firstname, lastname, None)
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

    def insert_sql_user_data_registration \
                    (self, telegram_id, nickname, age, gender, location, bio, photo):
        self.cursor.execute(sql_queries.INSERT_USER_DATA_QUERY,
                            (None, telegram_id, nickname, age, gender, location, bio, photo)
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

    def sql_select_balance_referral(self, tg_id):
        self.cursor.row_factory = lambda cursor, row: {
            "balance": row[0],
        }
        return self.cursor.execute(
            sql_queries.SELECT_BALANCE_REFERRAL_QUERY,
            (tg_id,)
        ).fetchone()

    def sql_update_reference_link(self, link, owner):
        self.cursor.execute(
            sql_queries.UPDATE_REFERENCE_LINK_QUERY,
            (link, owner,)
        )
        self.connection.commit()

    def sql_select_user_link(self, tg_id):
        self.cursor.row_factory = lambda cursor, row: {
            "link": row[0],
        }
        return self.cursor.execute(
            sql_queries.SELECT_USER_LINK_QUERY, (tg_id,)
        ).fetchone()

    def sql_select_user_by_link(self, link):
        self.cursor.row_factory = lambda cursor, row: {
            "tg_id": row[0],
        }
        return self.cursor.execute(
            sql_queries.SELECT_USER_BY_LINK_QUERY,
            (link,)
        ).fetchone()

    def sql_update_balance(self, tg_id):
        print(tg_id)
        self.cursor.execute(
            sql_queries.UPDATE_USER_BALANCE_QUERY,
            (tg_id,)
        )
        self.connection.commit()

    def sql_insert_referral(self, owner, referral):
        self.cursor.execute(
            sql_queries.INSERT_REFERRAL_QUERY, (None, owner, referral,)
        )
        self.connection.commit()

    def sql_insert_balance_query(self, owner, amount):
        self.cursor.execute(
            sql_queries.INSERT_BALANCE_QUERY, (None, owner, amount)
        )
        self.connection.commit()

    def sql_select_balance_user(self, tg_id):
        self.cursor.execute(
            sql_queries.SELECT_BAN_USER_QUERY, (tg_id,)
        )
        self.connection.commit()

    def sql_select_referral_users(self, tg_id):
        self.cursor.execute(
            sql_queries.SELECT_REFERENCE_LIST, (tg_id,)
        )
        return self.cursor.fetchall()

