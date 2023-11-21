from doctest import master
from customtkinter import *
import tkinter as tk 
class AUTH:
    def __init__(self, parent):
        ### create the sign up and log in page
        self.on_log_in = True
        self.parent = parent
        self.main_frame=CTkFrame(master=parent)
        
        
        self.log_in_frame()
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        
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

        self.log_in.pack(fill=tk.BOTH, expand=True)
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
# create the home page
class LoggedIn:
    def __init__(self, parent):
        #selected item to view
        self.selected = "Home"
        # creating the pages
        self.side_bar = CTkFrame(master=parent, fg_color="white")
        self.main_page = CTkFrame(master=parent,fg_color="white" )
       
        
        # placing the pages
        self.side_bar.pack(fill=tk.Y, side=tk.LEFT, padx=5)
        self.side_bar.configure(width=200)
        self.main_page.pack(fill=tk.BOTH, expand=True, side=tk.RIGHT, padx=5)
        #where things are added to the frames
        self.side_bar_handler()
    #call the developers tab
    def dev(self):
        self.change("Developers")
    #calls the home page tab
    def home(self):
        self.change("Home")
    # calls the logout tab
    def log_o(self):
        self.change("Log Out")
    # to clear the frame
    def change(self, parent):
            self.selected = parent
            for frames in self.side_bar.winfo_children():
                frames.destroy()
            self.side_bar_handler()
    # write things that goes in to side bar
    def side_bar_handler(self):
        #list of menu lists for now
        self.menus = {"Home":CTkButton(master=self.side_bar, text="Home", fg_color="transparent", text_color="black", hover_color="gray", command=self.home), 
                      "Developers":CTkButton(master=self.side_bar, text="Developers", fg_color="transparent", text_color="black", hover_color="gray", command=self.dev),
                      "Log Out":CTkButton(master=self.side_bar, text="Log Out", fg_color="transparent", text_color="black", hover_color="gray", command=self.log_o)}
        self.side_bar.option_clear()
        
        for i in self.menus:
            if i == self.selected:
                self.menus[i]._bg_color = "pink"
                
            
            self.menus[i].pack(fill=tk.X, side=tk.TOP, padx=10, pady=10)

