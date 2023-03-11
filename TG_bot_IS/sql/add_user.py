import pyodbc
from dotenv import dotenv_values, load_dotenv
import os


def add_user(user_id, tg_id, chat_id):
    load_dotenv()
    connection_db = pyodbc.connect(r'Driver={SQL Server};Server='+os.getenv("SERVER")+';Database=TGbot;Trusted_Connection=yes;')
    curs = connection_db.cursor()
    curs.execute("INSERT INTO Users (UserID,TelegramID,ChatID) values(?,?,?)", user_id, tg_id, chat_id)
    connection_db.commit()

