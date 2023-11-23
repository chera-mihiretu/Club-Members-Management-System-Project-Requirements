from customtkinter import *
from actions import *
# The Main frame
class MainFrame(CTk):
    def __init__(self, title):
        CTk.__init__(self)
        self.title(title)
        self.geometry("600x400")
        self.minsize(600,400)
        # declaration of frames
        self.auth = AUTH(self)
    def plat(self):
        print("may be")

        
    
#Starting the main loop
if __name__ == "__main__":
    app = MainFrame("CMM")
    app.mainloop()