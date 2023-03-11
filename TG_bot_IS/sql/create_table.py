import pyodbc
from dotenv import dotenv_values, load_dotenv
import os


def create_table():
    load_dotenv()
    connection_db = pyodbc.connect(r'Driver={SQL Server};Server='+os.getenv("SERVER")+';Database=TGbot;Trusted_Connection=yes;')
    curs = connection_db.cursor()
    curs.execute('''IF NOT EXISTS 
                        (SELECT *
                        FROM sysobjects
                        WHERE name='Users')
                        CREATE TABLE Users (
                        UserID bigint NOT NULL PRIMARY KEY, TelegramID bigint NOT NULL, ChatID bigint NOT NULL, corp_email text, created_date datetime)
                        ''')
    connection_db.commit()
