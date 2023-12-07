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

ALTER_USER_TABLE_RL = """
ALTER TABLE telegram_users
ADD COLUMN REFERENCE_LINK TEXT
"""

INSERT_USER_QUERY = """
INSERT OR IGNORE INTO telegram_users VALUES (?,?,?,?,?,?)"""

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

CREATE_BAN_USER_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS ban_users
(
ID INTEGER PRIMARY KEY,
TELEGRAM_ID INTEGER,
COUNT INTEGER,
UNIQUE (TELEGRAM_ID)
)
"""

INSERT_BAN_USER_QUERY = """
INSERT INTO ban_users VALUES (?,?,?)
"""

SELECT_BAN_USER_QUERY = """
SELECT * FROM ban_users WHERE TELEGRAM_ID = ?
"""

SELECT_POTENTIAL_BAN_USERS = """
SELECT * FROM ban_users WHERE COUNT >= 2
"""

SELECT_ALL_TG_USERS = """
SELECT * FROM telegram_users
"""

UPDATE_BAN_USER_COUNT_QUERY = """
UPDATE ban_users SET COUNT = COUNT + 1 WHERE TELEGRAM_ID = ?
"""

CREATE_USER_DATA_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS user_data
(
ID INTEGER PRIMARY KEY,
TELEGRAM_ID INTEGER,
NICKNAME CHAR(10),
AGE INTEGER,
GENDER CHAR(50),
LOCATION TEXT,
BIO CHAR(200),
PHOTO TEXT,
UNIQUE (TELEGRAM_ID)
)
"""

INSERT_USER_DATA_QUERY = """
INSERT INTO user_data VALUES (?,?,?,?,?,?,?,?)
"""

CREATE_LIKE_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS like_forms
(
ID INTEGER PRIMARY KEY,
OWNER_TELEGRAM_ID INTEGER,
LIKER_TELEGRAM_ID INTEGER,
UNIQUE (OWNER_TELEGRAM_ID, LIKER_TELEGRAM_ID)
)
"""
INSERT_LIKE_FORM_QUERY = """
INSERT INTO like_forms VALUES (?,?,?)
"""

SELECT_ALL_USER_DATA = """
SELECT * FROM user_data
"""

SELECT_ONE_USER_DATA = """
SELECT * FROM user_data WHERE TELEGRAM_ID = ?
"""

FILTER_DATA_LIKE = """
SELECT * FROM user_data
LEFT JOIN like_forms ON user_data.TELEGRAM_ID = like_forms.OWNER_TELEGRAM_ID
AND like_forms.LIKER_TELEGRAM_ID = ?
WHERE like_forms.ID IS NULL
AND user_data.TELEGRAM_ID != ?
"""

CREATE_REFERRAL_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS referral_table
(
ID INTEGER PRIMARY KEY,
OWNER_TELEGRAM_ID INTEGER,
REFERRAL_TELEGRAM_ID INTEGER,
UNIQUE(OWNER_TELEGRAM_ID, REFERRAL_TELEGRAM_ID)
)
"""
INSERT_REFERRAL_QUERY = """
INSERT INTO referral_table VALUES (?,?,?)
"""

SELECT_BALANCE_REFERRAL_QUERY = """
SELECT
    COALESCE(balance_query.BALANCE, 0) AS BALANCE
FROM 
    balance_query
LEFT JOIN
    referral_table ON balance_query.TELEGRAM_ID = referral_table.OWNER_TELEGRAM_ID
WHERE
     balance_query.TELEGRAM_ID = ?
"""

UPDATE_REFERENCE_LINK_QUERY = """
UPDATE telegram_users SET REFERENCE_LINK = ? WHERE TELEGRAM_ID = ?
"""

UPDATE_USER_BALANCE_QUERY = """
UPDATE balance_query SET BALANCE = COALESCE(BALANCE, 0) + 100 WHERE TELEGRAM_ID = ?
"""

SELECT_USER_LINK_QUERY = """
SELECT REFERENCE_LINK FROM telegram_users WHERE TELEGRAM_ID = ?
"""
SELECT_USER_BY_LINK_QUERY = """
SELECT TELEGRAM_ID FROM telegram_users WHERE REFERENCE_LINK = ?
"""

SELECT_REFERENCE_LIST = """
SELECT * FROM referral_table WHERE OWNER_TELEGRAM_ID = ?
"""

CREATE_BALANCE_QUERY = """
CREATE TABLE IF NOT EXISTS balance_query
(
ID INTEGER PRIMARY KEY,
TELEGRAM_ID INTEGER,
BALANCE INTEGER,
FOREIGN KEY (TELEGRAM_ID) REFERENCES referral_table(OWNER_TELEGRAM_ID),
UNIQUE(TELEGRAM_ID)
)
"""

INSERT_BALANCE_QUERY = """
INSERT INTO balance_query VALUES (?,?,?)
"""

SELECT_COUNT_BAN_QUERY = """
SELECT COUNT FROM ban_users WHERE TELEGRAM_ID = ?
"""

CHECK_CALLBACK_QUERY = """
SELECT COUNT(*) FROM callback_query WHERE TELEGRAM_ID = ?
"""

DELETE_DATA_CALLBACK_QUERY = """
DELETE FROM callback_query WHERE TELEGRAM_ID = ?"""

CREATE_NEWS_QUERY = """
CREATE TABLE IF NOT EXISTS news_query
(
ID INTEGER PRIMARY KEY,
LINK TEXT,
UNIQUE(LINK)
)
"""

INSERT_NEWS_QUERY = """
INSERT OR IGNORE INTO news_query VALUES (?,?)
"""

CREATE_FAVORITE_NEWS_QUERY = """
CREATE TABLE IF NOT EXISTS favorite_news_query (
ID INTEGER PRIMARY KEY,
LINK TEXT,
OWNER_TELEGRAM_ID INTEGER,
UNIQUE (LINK)
)

"""

INSERT_FAVORITE_NEWS_QUERY = """
INSERT INTO favorite_news_query VALUES (?,?,?)
"""

SELECT_ARTICLE_ID = """
SELECT ID FROM news_query WHERE LINK = ?;
"""
SELECT_ARTICLE_LINK = """
SELECT LINK FROM news_query WHERE ID = ?;
"""

CREATE_SCRAPED_NEWS_QUERY = """
CREATE TABLE IF NOT EXISTS scraped_news (
ID INTEGER PRIMARY KEY,
LINK TEXT
)
 """

INSERT_SCRAPED_NEWS_QUERY = """
INSERT INTO scraped_news VALUES (?,?)
"""

CREATE_SURVEY_QUERY = """
CREATE TABLE IF NOT EXISTS survey_query (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    IDEA TEXT,
    PROBLEMS TEXT,
    TELEGRAM_ID INTEGER,
    UNIQUE(TELEGRAM_ID)
)

"""

INSERT_SURVEY_QUERY = """
INSERT INTO survey_query VALUES (?, ?, ?, ?)
"""


GET_ALL_SURVEYS = """
SELECT * FROM survey_query
"""

GET_SURVEY_BY_ID = """
SELECT IDEA, PROBLEMS FROM survey_query WHERE ID = ?
"""
GET_IDEAS = """
SELECT IDEA FROM survey_query
"""

GET_PROBLEMS = """
SELECT PROBLEMS FROM survey_query
"""
