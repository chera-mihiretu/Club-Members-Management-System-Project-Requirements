import sqlite3
import math
import app_constants as ac
import encrption as crpt
import validator as vald
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
        raise vald.DatabaseError("No such user found, Please check your inputs")
    #register user
    def register_user(self, name, user_name, email, pass_word):
        value = self.cursor.execute(f"""
            SELECT {ac.USER_TABLE_ATTRIBUTE[0]} FROM {ac.USER_TABLE}
            WHERE {ac.USER_TABLE_ATTRIBUTE[0]} = "{user_name}" or {ac.USER_TABLE_ATTRIBUTE[2]} = "{email}"
        """).fetchall()
        if value != []:
            raise vald.DatabaseError("We found user with same user name or email please change the email or user_name")
        
        self.cursor.execute(f"""
            INSERT INTO {ac.USER_TABLE} ({ac.USER_TABLE_ATTRIBUTE[0]},
            {ac.USER_TABLE_ATTRIBUTE[1]},
            {ac.USER_TABLE_ATTRIBUTE[2]},
            {ac.USER_TABLE_ATTRIBUTE[3]})
            VALUES ("{user_name}","{name}","{email}","{crpt.hash_it(pass_word)}")
        """)


    #close the database
    def close_db(self):
        self.connection.commit
        self.connection.close()

    # close when the object is destroyed in any case
    def __del__(self):
        self.close_db()

       