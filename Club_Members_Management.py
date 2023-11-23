from customtkinter import *
from actions import *
# The Main frame
class MainFrame(CTk):
    def __init__(self, title):
        CTk.__init__(self)
        self.title(title)
        self.geometry("400x400")
        self.minsize(400,400)
        # declaration of frames
        self.auth = Admin(self)
        
        
    
#Starting the main loop
if __name__ == "__main__":
    app = MainFrame("CMM")
    app.mainloop()