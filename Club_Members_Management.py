from customtkinter import *
from actions import *
import app_constants as ac
# The Main frame
class MainFrame(CTk):
    def __init__(self, title):
        CTk.__init__(self)
        self.title(title)
        self.geometry(ac.WINDOW_SIZE)
        self.minsize(ac.FRAME_X, ac.FRAME_Y)
        # declaration of frames
        self.auth = AUTH(self)
        # handling situation like closing database when window is closed #
        self.bind("<Destroy>", lambda event:self.close_files())
    def plat(self):
        print("may be")
    # calling the destructer function  in such way we can close the databse #
    def close_files(self):
        # This function is called multiple times when the window is closed
        # so after it deleted it, again it will try to delete it, but the object is already deleted
        # in that case we face undefined object exception that is why we need to handle 
        # the exception
        try:
            self.auth.data_base.close_db()
            del self.auth
        except Exception as e:
            # just print the exception to the console
            print (e)

    

        
    
#Starting the main loop
if __name__ == "__main__":
    app = MainFrame("CMM")
    app.mainloop()
    