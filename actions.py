from struct import pack
from textwrap import fill
from turtle import bgcolor
from customtkinter import *
import tkinter as tk 
class LogIn(CTkFrame):
    def __init__(self, parent):
        self.parent = parent
        CTkFrame.__init__(self, parent, fg_color="#f0f9f9")
        
        
        
    #def create_frame(self):
        frame = CTkFrame(self, fg_color="white")
        name = CTkEntry(master=frame, placeholder_text="User Name")
        name.place(relx=.5, rely=.3,anchor="center")
     
        name = CTkEntry(master=frame, placeholder_text="Password")
        name.place(relx =.5, rely=.5, anchor="center")


        log_in = CTkButton(master=frame, text="Log In", command=self.to_display())
        log_in.place(relx=.5, rely=.7, anchor="center")
        frame.place(relx =.5, rely=.5, anchor="center")
       
        self.pack(fill=tk.BOTH, expand=True)
    def to_display(self):
        print("hahah")
    def show(self):
        pass#self.create_frame()
