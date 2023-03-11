from datetime import datetime
import pyodbc

def update_user(server_name, user_id, corp_email):
    connection_db = pyodbc.connect(r'Driver={SQL Server};Server='+server_name+';Database=TGbot;Trusted_Connection=yes;')
    curs = connection_db.cursor()
    created_date = datetime.now()
    sql = "UPDATE Users SET corp_email=?, created_date=? WHERE UserID=?".format()
    curs.execute(sql, corp_email, created_date, user_id)
    connection_db.commit()
