import mysql.connector
from configparser import ConfigParser

#Read config.ini file
config_object = ConfigParser()
config_object.read("config.ini")

DB_info = config_object["SERVERCONFIG"]

class Database():
    def __init__(self):
        self.conn = mysql.connector.connect(
            host = DB_info["host"],
            user = DB_info["user"],
            password = DB_info["password"],
            database = DB_info["database"]
        )
            
    def GetAll(self, SQLquery, array=()):
        cursor = self.conn.cursor()
        cursor.execute(SQLquery, array)
        return cursor.fetchall()

    def GetOne(self, SQLquery, array=()):
        cursor = self.conn.cursor()
        cursor.execute(SQLquery, array)
        return cursor.fetchone()

    def Execute(self, SQLquery, array=()):
        cursor = self.conn.cursor()
        cursor.execute(SQLquery, array)
        self.conn.commit()
        return cursor.rowcount

    def deConnect(self):
        self.conn.close()