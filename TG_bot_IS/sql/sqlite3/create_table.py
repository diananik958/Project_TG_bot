import sqlite3
from dotenv import load_dotenv
import os


def create_table():
    load_dotenv()
    connection_db = sqlite3.connect(os.getenv("PATH_DB"))
    curs = connection_db.cursor()
    curs.execute("""CREATE TABLE IF NOT EXISTS Users(
       UserID INTEGER PRIMARY KEY AUTOINCREMENT,
       TelegramID INT NOT NULL,
       corp_email TEXT,
       created_date TEXT);
    """)
    connection_db.commit()
