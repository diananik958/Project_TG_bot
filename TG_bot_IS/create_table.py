import pyodbc

def create_table(server_name):
    connection_db = pyodbc.connect(r'Driver={SQL Server};Server='+server_name+';Database=TGbot;Trusted_Connection=yes;')
    curs = connection_db.cursor()
    curs.execute('''IF NOT EXISTS 
                        (SELECT *
                        FROM sysobjects
                        WHERE name='Users')
                        CREATE TABLE Users (
                        UserID bigint NOT NULL PRIMARY KEY, TelegramID bigint NOT NULL, ChatID bigint NOT NULL, corp_email text, created_date datetime)
                        ''')
    connection_db.commit()
