from customtkinter import CTkFrame, CTkEntry, CTkButton, CTkInputDialog, CTkScrollableFrame, CTkLabel, CTkImage
from PIL import Image
import tkinter as tk
import os
import app_constants as ac
import validator as vald
###################################################
########### Create Inv for users ##################
###################################################
class LoggedIn:
    def __init__(self, parent, database, status):

        #selected item to view
        self.status = status
        self.database = database
        self.parent = parent
        self.selected = "Home"
        self.frame_dictionary = {}
        self.menus_items = {}
        # creating the pages
        self.side_bar = CTkFrame(master=parent, fg_color=ac.FG_COLOR, corner_radius=0)
        self.main_page = CTkFrame(master=parent,fg_color=ac.WHITE_BG, corner_radius=10)
        self.menus = {"Home":lambda:self.change("Home"), "Developers":lambda:self.change("Developers"), "Profile":lambda:self.change("Profile"), "Log Out":lambda:self.change("Log Out")}
        self.menus_page = {"Home":self.home_page, "Developers":self.dev_page, "Profile":self.profile_page, "Log Out":self.log_out_page}
        
        

    def show(self):
        # placing the pages
        self.side_bar.pack(fill=tk.Y, side=tk.LEFT)
        self.side_bar.configure(width=200)
        self.main_page.pack(fill=tk.BOTH, expand=True, side=tk.RIGHT, padx=5, pady=5)
        #where things are added to the frames
        self.side_bar_handler()
    
    
    # to clear the frame
    def change(self, parent):
        
        self.selected = parent
        #clearing the main frame
        for frames  in self.main_page.winfo_children():
            frames.destroy()
        #clearing the side bar for the button to update
        for frames in self.side_bar.winfo_children():
            frames.destroy()
            

        self.side_bar_handler()
    # write things that goes in to side bar
    def side_bar_handler(self):
        #make the page that is active visible and recreate them
        
        self.frame_dictionary = {}
        for frames in self.menus.keys():
            self.frame_dictionary[frames] = CTkScrollableFrame(master=self.main_page, fg_color=ac.WHITE_BG)
            if frames == self.selected:
                self.frame_dictionary[frames].pack(fill=tk.BOTH, expand=True)
        self.menus_page[self.selected](self.frame_dictionary[self.selected])
        # recreate the buttons
        #list of menu lists for now
        self.menus_items = {}
        
        for item in self.menus.keys():
            
            if item == self.selected:
                self.menus_items[item] = CTkButton(master=self.side_bar, text=item, fg_color=ac.BLUE_BG,text_color=ac.WHITE_BG, hover_color=ac.BLUE_BG, command=self.menus[item],border_spacing=0)
                continue
            self.menus_items[item] = CTkButton(master=self.side_bar, text=item, fg_color="transparent",text_color=ac.WHITE_BG, hover_color=ac.BLUE_BG, command=self.menus[item],border_spacing=0)

        #self.side_bar.option_clear()
        for i in self.menus_items.keys():
            if i == self.selected:
                self.menus_items[i]._bg_color = ac.BLUE_BG
            self.menus_items[i].pack(fill=tk.X, side=tk.TOP, pady=5, padx=5)
    
    ##################################################################
    ######################create page contents########################
    ##################################################################
    def home_page(self, parent):
        value = self.database.extract_post()
        if value != []:
            for post_id, post_title, post_desc, url in value:
                self.single_post(self.frame_dictionary[self.selected], 
                                 post_id, vald.short(post_title),vald.short(post_desc), url)
    def dev_page(self, parent):
        value = self.database.extract_devs()
        if value != []:
            for user_name, name,email in value:
                if user_name == self.status.get_user_name() or user_name=="admin":
                    continue
                self.single_dev(self.frame_dictionary[self.selected], name, user_name, ac.DEV_ICON)
    def profile_page(self, parent):
        infos = {"user_age":"Age", "user_p_l":"Programming Language",  "user_work_place":"Work Place"}
        inputs = {}
        for i in infos.keys():
            inputs[i] = CTkEntry(master=parent, placeholder_text=infos[i])
            inputs[i].pack(ipadx=50,ipady=5,padx=10,pady=10,expand=False, side=tk.TOP)
        warning = CTkLabel(master=parent, text="If You have already entered your info before know that it will be overwritten", text_color="red")
        warning.pack(side=tk.TOP, pady=10)
        add_info = CTkButton(master=parent, text="Update/Enter", command=lambda:self.update_info( inputs))
        add_info.pack(side=tk.TOP, pady=10)
    def log_out_page(self, parent):
        warning = CTkLabel(master=parent, text="Are you sure you wanna log out!", text_color="red")
        warning.pack(side=tk.TOP, pady=10)
        yes = CTkButton(master=parent, text="YES", fg_color=ac.FG_COLOR, command=self.log_out)
        yes.pack(side=tk.TOP, pady=10)
        no = CTkButton(master=parent, text="No", fg_color=ac.FG_COLOR, command=lambda:self.change("Home"))
        no.pack(side=tk.TOP, pady=10)
    def log_out(self):
        self.parent.log_out()
    def update_info(self, inputs):
        
        self.database.add_more_info(self.status.get_user_name(),
                                    inputs[ac.USERS_INFO_TABLE_ATTRIBUTES[1]].get(),
                                    inputs[ac.USERS_INFO_TABLE_ATTRIBUTES[2]].get(),
                                    inputs[ac.USERS_INFO_TABLE_ATTRIBUTES[3]].get())

    def single_dev(self, parent, name, user_name,  url="dev_icon.png"):
        frame_holder = CTkFrame(master=parent, fg_color="transparent")
        frame = CTkFrame(master=frame_holder,fg_color=ac.FG_COLOR)
        frame_info = CTkFrame(master=frame, fg_color="transparent")
        
        name = CTkLabel(master=frame_info, text=name, font=("Normal", 12), text_color=ac.WHITE_BG)
        user_name = CTkLabel(master=frame_info, text="@"+user_name, font=("Normal", 12), text_color=ac.WHITE_BG)
        name.pack(expand=False, padx=5, pady=5, side=tk.TOP)
        user_name.pack(expand=False, padx=5, pady=5, side=tk.TOP)
        img = CTkImage(light_image=Image.open(url), size=(40,40))
        img_= CTkLabel(master=frame, image=img, text="")
        img_.pack(expand=False, side=tk.LEFT, padx=10)

        frame.pack(expand=False, side=tk.LEFT, fill=tk.X, ipadx=10)
        frame_info.pack(expand=False, side=tk.LEFT)
        frame_holder.pack(expand=False, padx=10, pady = 10, side=tk.TOP, fill=tk.X)


    def single_post(self, parent,post_id, title="", desc="", url=""):
        #check if the image actually exists
        file_exist = os.path.exists(url)
        #create a page to display all posted ifos
        frame_holder = CTkFrame(master=parent, fg_color="transparent",bg_color="transparent")
        frame = CTkFrame(master=frame_holder, fg_color=ac.FG_COLOR, corner_radius=10,bg_color="transparent")
        frames_to_dis = [CTkFrame(master=frame, fg_color="transparent",bg_color="transparent") for i in range(3)]
        t_text = CTkLabel(master=frames_to_dis[0], text=title, text_color=ac.WHITE_BG,bg_color="transparent",font=("Bold", 15))
        t_text.pack(padx=10,expand=False, side=tk.LEFT)
        m_text = CTkLabel(master=frames_to_dis[1], text=desc, text_color=ac.WHITE_BG,bg_color="transparent",font=("Normal", 10), justify=tk.LEFT)
        m_text.pack(padx=10,expand=False, side=tk.LEFT)
        #viw an image if the image is posted
        img = None
        if file_exist:
            img = CTkImage(light_image=Image.open(url), size=(300,300))
            img_= CTkLabel(master=frames_to_dis[2], image=img,bg_color="transparent", text="")
            img_.pack(expand=False, side=tk.LEFT)
        for i in range(len(frames_to_dis)):
            if i == 2:
                if not file_exist:
                    continue

            frames_to_dis[i].pack(fill=tk.X, expand=False,side=tk.TOP)
        frame.pack(expand=False, padx=10, pady=10,ipadx=80,side=tk.LEFT)
        frame_holder.pack(expand=False, fill=tk.X, side=tk.TOP)