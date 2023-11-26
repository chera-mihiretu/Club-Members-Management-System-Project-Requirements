from atexit import register
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
    ###############################################################
    ################## start by creating default tables ###########
    ###############################################################
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
            {} TEXT,
            {} TEXT
           ); 
        """.format(ac.USERS_INFO_TABLE,
                   ac.USERS_INFO_TABLE_ATTRIBUTES[0],
                   ac.USERS_INFO_TABLE_ATTRIBUTES[1],
                   ac.USERS_INFO_TABLE_ATTRIBUTES[2],
                   ac.USERS_INFO_TABLE_ATTRIBUTES[3]))
        self.commit()
        #######################################################
        ##### just to make it easy admin password #############
        #######################################################
        try:
            self.register_user("admin", "admin", "admin", "admin_password")
        except vald.DatabaseError as e:
            print(e)
        self.connection.commit()

        
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
            raise vald.DatabaseError("No such user found, Please check your inputs")
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
        self.commit()
    #delete a user from data base admin capability
    def delete_user(self, user_name):
        self.cursor.execute(f"""
            DELETE FROM {ac.USER_TABLE} WHERE {ac.USER_TABLE_ATTRIBUTE[0]} = "{user_name}";
        """)
        self.connection.commit()
        self.cursor.execute(f"""
            SELECT * FROM {ac.USERS_INFO_TABLE} WHERE {ac.USERS_INFO_TABLE_ATTRIBUTES[0]}="{user_name}";
        """)
        if self.cursor.fetchall() == []:
            return
        self.cursor.execute(f"""
            DELETE FROM {ac.USERS_INFO_TABLE} WHERE {ac.USERS_INFO_TABLE_ATTRIBUTES[0]} = "{user_name}";
        """)
        self.connection.commit()

    #extract posts from database
    def extract_post(self):
        self.cursor.execute(f"""
            SELECT * FROM {ac.POST_TABLE}
        """)

        value =  self.cursor.fetchall()
        if value == []:
            print("database is empty")
        return value
    #extract developer from database
    def extract_devs(self):
        self.cursor.execute(f"""
            SELECT {ac.USER_TABLE_ATTRIBUTE[0]}, 
            {ac.USER_TABLE_ATTRIBUTE[1]},
            {ac.USER_TABLE_ATTRIBUTE[2]} FROM {ac.USER_TABLE}
        """)

        value =  self.cursor.fetchall()
        if value == []:
            print("database is empty")
        
        return value
       
    #adding more information to user
    def add_more_info(self, user_name, user_age, prog_lang, organ):
        value = self.cursor.execute(f"""
        SELECT * FROM Users_Info
        WHERE "{ac.USERS_INFO_TABLE_ATTRIBUTES[0]}" = "{user_name}"
        """).fetchall()
        
        if value == []:
            self.cursor.execute(f"""
                INSERT INTO "{ac.USERS_INFO_TABLE}" (
                "{ac.USERS_INFO_TABLE_ATTRIBUTES[0]}",
                "{ac.USERS_INFO_TABLE_ATTRIBUTES[1]}",
                "{ac.USERS_INFO_TABLE_ATTRIBUTES[2]}",
                "{ac.USERS_INFO_TABLE_ATTRIBUTES[3]}")
                VALUES("{user_name}",
                {user_age}, "{prog_lang}", "{organ}")
                """)
            print("inserted")
            self.commit()
            return
       
        self.cursor.execute(f"""
            UPDATE {ac.USERS_INFO_TABLE}
            SET 
            {ac.USERS_INFO_TABLE_ATTRIBUTES[0]}="{user_name}",
            {ac.USERS_INFO_TABLE_ATTRIBUTES[1]}="{user_age}",
            {ac.USERS_INFO_TABLE_ATTRIBUTES[2]}="{prog_lang}",
            {ac.USERS_INFO_TABLE_ATTRIBUTES[3]}="{organ}"
            WHERE {ac.USERS_INFO_TABLE_ATTRIBUTES[0]} = "{user_name}"
         
        """)
        print("updated")


        self.commit()
    # creating a post
    def create_post(self, post_title, post_desc, url=""):
        self.cursor.execute(f"""
            INSERT INTO {ac.POST_TABLE} (
            {ac.POST_TABLE_ATTRIBUTE[1]},
            {ac.POST_TABLE_ATTRIBUTE[2]},
            {ac.POST_TABLE_ATTRIBUTE[3]}
            )
            VALUES ("{post_title}", "{post_desc}", "{url}")
        """)
        self.connection.commit()
    #deleting post 
    def delete_post(self, p_id):
        self.cursor.execute(f"""
            DELETE FROM {ac.POST_TABLE} WHERE {ac.POST_TABLE_ATTRIBUTE[0]} = "{p_id}"
        """)
        self.connection.commit()
    #close the database
    def commit(self):
        self.connection.commit()
    def close_db(self):
        
        self.connection.commit
        self.connection.close()

    # close when the object is destroyed in any case
    def __del__(self):
        self.close_db()

       