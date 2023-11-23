from customtkinter import CTkFrame, CTkEntry, CTkButton, CTkInputDialog
import tkinter as tk 
class Admin:
    def __init__(self, parent):
        self.parent = parent
        # creating the pages
        self.side_bar = CTkFrame(master=parent, fg_color="#1A0301")
        self.main_page = CTkFrame(master=parent,fg_color="white" )
        # placing the pages
        self.side_bar.pack(fill=tk.Y, side=tk.LEFT, padx=5)
        self.side_bar.configure(width=200)
        self.main_page.pack(fill=tk.BOTH, expand=True, side=tk.RIGHT, padx=5)
        #where things are added to the frames
        self.side_bar_handler(self.side_bar)
    def side_bar_handler(self, parent):
        pass
