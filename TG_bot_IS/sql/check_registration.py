import pyodbc
from dotenv import dotenv_values, load_dotenv
import os


def check_user(user_id):
    load_dotenv()
    connection_db = pyodbc.connect(r'Driver={SQL Server};Server='+os.getenv("SERVER")+';Database=TGbot;Trusted_Connection=yes;')
    curs = connection_db.cursor()
    sql = '''SELECT TelegramID, ChatID, corp_email FROM Users WHERE UserID=?'''.format()
    curs.execute(sql, user_id)
    result = curs.fetchone()    # fetchall
    return str(result)

