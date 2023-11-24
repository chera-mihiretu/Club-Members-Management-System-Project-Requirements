import sqlite3
import math
import app_constants as ac
class DataBase:
    def __init__(self):

        self.connection = sqlite3.connect("database.db")

        self.cursor = self.connection.cursor()
        
        self.create_neccesary_table_if_not_exist()
       
    def create_neccesary_table_if_not_exist(self):
        self.cursor.execute("""
           CREATE TABLE IF NOT EXISTS {} (
            {} TEXT UNIQUE PRIMARY KEY NOT NULL,
            {} TEXT NOT NULL,
            {} TEXT NOT NULL,
            {} TEXT NOT NULL
           );
        """.format(ac.USER_TABLE, 
                   ac.USER_TABLE_ATTRIBUTE[0],
                   ac.USER_TABLE_ATTRIBUTE[1],
                   ac.USER_TABLE_ATTRIBUTE[2],
                   ac.USER_TABLE_ATTRIBUTE[3]))
        self.cursor.execute(
        """
          CREATE TABLE IF NOT EXISTS {} (
            {} INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT,
            {} TEXT NOT NULL,
            {} TEXT NOT NULL,
            {} TEXT
           );   
        """.format(ac.POST_TABLE,
                   ac.POST_TABLE_ATTRIBUTE[0],
                   ac.POST_TABLE_ATTRIBUTE[1],
                   ac.POST_TABLE_ATTRIBUTE[2],
                   ac.POST_TABLE_ATTRIBUTE[3]))
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS {} (
            {} TEXT UNIQUE PRIMARY KEY NOT NULL,
            {} INTEGER,
            {} CHAR,
            {} TEXT,
            {} TEXT
           ); 
        """.format(ac.USERS_INFO_TABLE,
                   ac.USERS_INFO_TABLE_ATTRIBUTES[0],
                   ac.USERS_INFO_TABLE_ATTRIBUTES[1],
                   ac.USERS_INFO_TABLE_ATTRIBUTES[2],
                   ac.USERS_INFO_TABLE_ATTRIBUTES[3],
                   ac.USERS_INFO_TABLE_ATTRIBUTES[4]))
    #close the database
    def close_db(self):
        self.connection.commit
        self.connection.close()

    # close when the object is destroyed in any case
    def __del__(self):
        self.close_db()
       