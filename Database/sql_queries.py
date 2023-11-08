CREATE_USER_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS telegram_users
(
ID INTEGER PRIMARY KEY,
TELEGRAM_ID INTEGER,
USERNAME CHAR(50),
FISRT_NAME CHAR(50),
LAST_NAME CHAR(50),
UNIQUE (TELEGRAM_ID)
)
"""

INSERT_USER_QUERY = """
INSERT OR IGNORE INTO telegram_users VALUES (?,?,?,?,?)"""

CREATE_CALLBACK_QUERY = """
CREATE TABLE IF NOT EXISTS callback_query
(
ID INTEGER PRIMARY KEY,
TELEGRAM_ID INTEGER,
ANSWER TEXT DEFAULT NULL,
UNIQUE (TELEGRAM_ID),
FOREIGN KEY (TELEGRAM_ID) REFERENCES telegram_users(TELEGRAM_ID)
)
"""
INSERT_CALLBACK_QUERY = """
INSERT OR IGNORE INTO callback_query VALUES (?, ?, ?)"""
