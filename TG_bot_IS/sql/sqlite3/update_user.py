from datetime import datetime
import sqlite3
from dotenv import dotenv_values, load_dotenv
import os


def update_user(user_id, corp_email):
    load_dotenv()
    connection_db = sqlite3.connect(os.getenv("PATH_DB"))
    curs = connection_db.cursor()
    created_date = datetime.now()
    sql = "UPDATE Users SET corp_email=?, created_date=? WHERE TelegramID=?"
    curs.execute(sql, (corp_email, created_date, user_id))
    connection_db.commit()
