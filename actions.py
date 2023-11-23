
from customtkinter import CTkFrame, CTkEntry, CTkButton, CTkInputDialog
import tkinter as tk
from PIL import Image
from LoggedIn import *
from Admin import *
class AUTH:
    def __init__(self, parent):
        ### create the sign up and log in page
        self.on_log_in = True
        self.parent = parent
        self.main_frame=CTkFrame(master=parent)
        
        
        self.log_in_frame()
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        self.admin= None

        
        
    #create the log frame
    def log_in_frame(self):
        #create contents
        self.log_in = CTkFrame(master=self.main_frame, fg_color="white")
        user_name = CTkEntry(master=self.log_in, placeholder_text="User Name")
        pass_word = CTkEntry(master=self.log_in, placeholder_text="Password")
        log_in = CTkButton(master=self.log_in, text="Log In")
        no_acc = CTkButton(master=self.log_in, text="Have No Account", command=self.change_frame, text_color="black",fg_color="transparent", border_spacing=2)
        #placing the contents
        user_name.place(relx=.5, rely=.3, anchor="center")
        pass_word.place(relx=.5, rely=.4, anchor="center")
        log_in.place(relx=.5, rely=.5, anchor="center")
        no_acc.place(relx=.5, rely=.6, anchor="center" )
        #creating the admin button
        self.admin_btn(self.log_in)

        self.log_in.pack(fill=tk.BOTH, expand=True)
    def admin_log_in(self):
        dialog = CTkInputDialog(title="Admin", text="Password")
        
    def admin_btn(self, parent):
        self.admin = CTkButton(master=parent, text="Admin", fg_color="transparent", text_color="black", border_color="#170A17", border_width=1,command=self.admin_log_in)
        self.admin.place(relx=.9, rely=.1, anchor="center")
    #cereate the sign in frame
    def sign_up_frame(self):
        #create contents
        self.sign_up = CTkFrame(master=self.main_frame, fg_color="white")
        user_name = CTkEntry(master=self.sign_up, placeholder_text="User Name")
        name = CTkEntry(master=self.sign_up, placeholder_text="Full Name")
        pass_word = CTkEntry(master=self.sign_up, placeholder_text="Password")
        confirm_pass_word = CTkEntry(master=self.sign_up, placeholder_text="Confirm Password")
        log_in = CTkButton(master=self.sign_up, text="Sign Up")
        no_acc = CTkButton(master=self.sign_up, text="Already Have Account", command=self.change_frame)
        #placing the contents
        name.place(relx=.5, rely=.3, anchor="center")
        user_name.place(relx=.5, rely=.4, anchor="center")
        pass_word.place(relx=.5, rely=.5, anchor="center")
        confirm_pass_word.place(relx=.5, rely=.6, anchor="center")
        log_in.place(relx=.5, rely=.7, anchor="center")
        no_acc.place(relx=.5, rely=.8, anchor="center" )
        #creating the admin button
        self.sign_up.pack(fill=tk.BOTH, expand=True)
    # this helps to toggle between the sign up and log in page
    def change_frame(self):
        for frames in self.main_frame.winfo_children():
            frames.destroy()
        if self.on_log_in:
            self.sign_up_frame()
            self.on_log_in = not self.on_log_in
        else:
            self.log_in_frame()
            self.on_log_in = not self.on_log_in

