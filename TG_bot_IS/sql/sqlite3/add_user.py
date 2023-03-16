import sqlite3
from dotenv import dotenv_values, load_dotenv
import os


def add_user(user_id, tg_id, chat_id):
    load_dotenv()
    connection_db = sqlite3.connect(os.getenv("PATH_DB"))
    curs = connection_db.cursor()
    curs.execute("INSERT INTO Users (UserID,TelegramID,ChatID) values(?,?,?);", (user_id, tg_id, chat_id))
    connection_db.commit()

