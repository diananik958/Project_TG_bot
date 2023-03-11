import pyodbc

def check_user(server_name, user_id):
    connection_db = pyodbc.connect(r'Driver={SQL Server};Server='+server_name+';Database=TGbot;Trusted_Connection=yes;')
    curs = connection_db.cursor()
    sql = "SELECT TelegramID, ChatID, corp_email FROM Users WHERE UserID=?".format()
    curs.execute(sql, user_id)
    result = curs.fetchone()   #fetchall
    return(result)

print(check_user(server_name, user_id))
