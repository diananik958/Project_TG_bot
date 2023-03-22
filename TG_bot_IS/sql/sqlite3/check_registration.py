import sqlite3
from dotenv import dotenv_values, load_dotenv
import os


def check_user(user_id):
    load_dotenv()
    connection_db = sqlite3.connect(os.getenv("PATH_DB"))
    curs = connection_db.cursor()
    sql = '''SELECT corp_email FROM Users WHERE TelegramID=?'''
    curs.execute(sql, (user_id, ))
    result = curs.fetchone()
    return str(result)

