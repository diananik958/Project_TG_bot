import pyodbc

def add_user(server_name, user_id, tg_id, chat_id):
    connection_db = pyodbc.connect(r'Driver={SQL Server};Server='+server_name+';Database=TGbot;Trusted_Connection=yes;')
    curs = connection_db.cursor()
    curs.execute("INSERT INTO Users (UserID,TelegramID,ChatID) values(?,?,?)", user_id, tg_id, chat_id)
    connection_db.commit()