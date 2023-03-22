import sqlite3
from dotenv import dotenv_values, load_dotenv
import os


def add_user(tg_id):
    load_dotenv()
    connection_db = sqlite3.connect(os.getenv("PATH_DB"))
    curs = connection_db.cursor()
    curs.execute("INSERT INTO Users (TelegramID) values(?);", (tg_id, ))
    connection_db.commit()

