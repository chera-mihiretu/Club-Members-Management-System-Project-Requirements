####################################################################
# this is are some constants that are used through out the program #
####################################################################
local_data_path = "cmm.data"
FG_COLOR = "#170A17"
HOVER_COLOR = "#DB9167"
WHITE_BG = "#E7E7FC"
BLUE_BG = "#0088FF"
TITLE = "CMM"
WINDOW_SIZE = "600x400"
FRAME_X:int = 600
FRAME_Y:int = 400
DATABSE_NAME = "DATABASE"
USER_TABLE = "Users"
POST_TABLE = "Posts"
USERS_INFO_TABLE = "Users_Info"
USER_TABLE_ATTRIBUTE = ["user_name", "full_name", "email", "user_password"]
POST_TABLE_ATTRIBUTE = ["post_id", "post_title", "post_desc", "url"]
USERS_INFO_TABLE_ATTRIBUTES = ["user_name", "user_age", "user_gender", "user_p_l", "user_work_place"]
class Status:
    def __init__(self, user_name:str=None):
        self.__user_name = user_name
    #### using setter function because they cannot be changed in direct access ####
    def set_user_name(self, user_name):
        self.__user_name = user_name
    #### using setter function because they cannot be  accessed directly ####
    def get_user_name(self):
        return self.__user_name
