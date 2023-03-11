from datetime import datetime
import pyodbc
from dotenv import dotenv_values, load_dotenv
import os


def update_user(user_id, corp_email):
    load_dotenv()
    connection_db = pyodbc.connect(r'Driver={SQL Server};Server='+os.getenv("SERVER")+';Database=TGbot;Trusted_Connection=yes;')
    curs = connection_db.cursor()
    created_date = datetime.now()
    sql = "UPDATE Users SET corp_email=?, created_date=? WHERE UserID=?".format()
    curs.execute(sql, corp_email, created_date, user_id)
    connection_db.commit()
