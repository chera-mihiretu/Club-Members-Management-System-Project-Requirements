import sqlite3
import math
import app_constants as ac
import encrption as crpt
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
    # check if user exists
    def user_exist(self, user_name, password):
        
        value = self.cursor.execute("""
            SELECT {}, {}  FROM {}
            WHERE {} = "{}"
        """.format(ac.USER_TABLE_ATTRIBUTE[0],
                   ac.USER_TABLE_ATTRIBUTE[3],
                   ac.USER_TABLE, 
                   ac.USER_TABLE_ATTRIBUTE[0], 
                   user_name))
        value = value.fetchall()
        print(value)
        print([(user_name, "{}".format(crpt.hash_it(password)))])
        if value == []:
            return False
        elif value == [(user_name, "{}".format(crpt.hash_it(password)))]:
            return True
        return False
        

    #close the database
    def close_db(self):
        self.connection.commit
        self.connection.close()

    # close when the object is destroyed in any case
    def __del__(self):
        self.close_db()

       