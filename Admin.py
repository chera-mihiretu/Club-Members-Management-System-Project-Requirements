from customtkinter import *
import tkinter as tk 
from PIL import Image
import app_constants as ac
class Admin:
    def __init__(self, parent):
        self.parent = parent
        # creating the pages
        self.side_bar = CTkFrame(master=parent, fg_color=ac.FG_COLOR, corner_radius=0)
        self.main_page = CTkFrame(master=parent,fg_color=ac.WHITE_BG, corner_radius=10)
        

        #selected item to view
        self.selected = "Developers"
        self.frame_dictionary = {}
        self.menus_items = {}
        # creating the menus available for admin
        self.menus = {"Developers":lambda:self.change("Developers"), "Posts":lambda:self.change("Posts"), "Create Post":lambda:self.change("Create Post"), "Log Out":lambda:self.change("Log Out")}
        self.menus_page = {"Developers":self.dev_page, "Posts":self.post_page,"Create Post":self.create_post,"Log Out":self.log_out_page}
        
        

    def show(self):
        # placing the pages
        self.side_bar.pack(fill=tk.X, side=tk.TOP, ipadx=5, ipady=5)
        self.side_bar.configure(height=40)
        self.main_page.pack(fill=tk.BOTH, expand=True, side=tk.TOP, padx=5)
        #where things are added to the frames
        self.side_bar_handler()
    def change(self, parent):
        self.selected = parent
        #clearing the main frame
        for frames  in self.main_page.winfo_children():
            frames.destroy()
        #clearing the side bar for the button to update
        for frames in self.side_bar.winfo_children():
            frames.destroy()
        #rearrange things
        self.side_bar_handler()
    def side_bar_handler(self):
        #make the page that is active visible and recreate them
        
        self.frame_dictionary = {}
        for frames in self.menus.keys():
            self.frame_dictionary[frames] = CTkScrollableFrame(master=self.main_page, fg_color=ac.WHITE_BG, scrollbar_button_color=ac.FG_COLOR)
            if frames == self.selected:
                self.frame_dictionary[frames].pack(fill=tk.BOTH, expand=True)
        self.menus_page[self.selected](self.frame_dictionary[self.selected])
        # recreate the buttons
        #list of menu lists for now
        self.menus_items = {}
        
        for item in self.menus.keys():
            if item == self.selected:
                self.menus_items[item] = CTkButton(master=self.side_bar, text=item, 
                                                  fg_color=ac.BLUE_BG,text_color=ac.WHITE_BG, hover_color=ac.BLUE_BG, 
                                                   command=self.menus[item],border_spacing=0)
                continue
            self.menus_items[item] = CTkButton(master=self.side_bar, text=item, 
                                               fg_color="transparent",text_color=ac.WHITE_BG, hover_color=ac.BLUE_BG, 
                                               command=self.menus[item],border_spacing=0)

        #self.side_bar.option_clear()
        for i in self.menus_items.keys():
            if i == self.selected:
                self.menus_items[i]._bg_color = ac.BLUE_BG
            self.menus_items[i].pack(fill=tk.X, side=tk.LEFT, pady=5)
    def dev_page(self, parent):
        for i in range(23):
            self.single_dev(self.frame_dictionary[self.selected], name="abdi", user_name_text="chera")
    def post_page(self, parent):
        pass
    def create_post(self, parent):
        #creating a post inviroment
        post_title = CTkEntry(master=parent, placeholder_text="Title")
        #post desc label
        desc = CTkLabel(master=parent, text="Desc...")
        #post desc input
        post_desc = CTkTextbox(master=parent, scrollbar_button_color=ac.FG_COLOR, fg_color="white")
        #choosing a file if it has a file
        choose_pic = CTkButton(master=parent, text="Add Picture")
        file_path = CTkLabel(master=parent, text=choose_pic)
        upload = CTkButton(master=parent, text="Upload")
        post_title.pack(side=tk.TOP, pady=10, ipadx=100)
        #adding the components to the frame
        desc.pack(side=tk.TOP, ipadx=80)
        post_desc.pack(side=tk.TOP, ipadx=60)
        choose_pic.pack(side=tk.TOP, pady=10)
        upload.pack(side=tk.TOP, pady=10)


    def log_out_page(self, parent):
        #creating a wirning dialog when log out
        warning = CTkLabel(master=parent, text="Are you sure you wanna log out!", text_color="red")
        warning.pack(side=tk.TOP, pady=10)
        yes = CTkButton(master=parent, text="YES", fg_color=ac.FG_COLOR, command=self.log_out)
        yes.pack(side=tk.TOP, pady=10)
        no = CTkButton(master=parent, text="No", fg_color=ac.FG_COLOR, command=lambda:self.change("Developers"))
        no.pack(side=tk.TOP, pady=10)
    def log_out(self):
        self.parent.log_out()
    def single_dev(self, parent, name, user_name_text,  url="dev_icon.png"):
        #create a frame a single that we can itrate through
        frame_holder = CTkFrame(master=parent, fg_color="transparent")
        frame = CTkFrame(master=frame_holder,fg_color=ac.FG_COLOR)
        frame_info = CTkFrame(master=frame, fg_color="transparent")
        #creating the components to display informations
        name = CTkLabel(master=frame_info, text=name, font=("Normal", 12), text_color=ac.WHITE_BG)
        user_name = CTkLabel(master=frame_info, text="@"+user_name_text, font=("Normal", 12), text_color=ac.WHITE_BG)
        img = CTkImage(light_image=Image.open(url), size=(40,40))
        img_= CTkLabel(master=frame, image=img, text="")
        #delete button to remove a developer from a database
        delete = CTkButton(master=frame, text="Remove", command=lambda:self.delete_user(frame_holder, user_name_text))
        #adding the components to the frame
        name.pack(expand=False, padx=5, pady=5, side=tk.TOP)
        user_name.pack(expand=False, padx=5, pady=5, side=tk.TOP)
        img_.pack(expand=False, side=tk.LEFT, padx=10)
        frame.pack(expand=False, side=tk.LEFT, fill=tk.X, ipadx=10)
        frame_info.pack(expand=False, side=tk.LEFT)
        delete.pack(expand=False, side=tk.RIGHT, padx=10)

        frame_holder.pack(expand=False, padx=10, pady = 10, side=tk.TOP, fill=tk.X)
    # deleting a user from database
    def delete_user(self, holder, user_name):
        print(user_name)
        holder.destroy()
    def single_post(self, parent,title="", desc="", url=""):
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
        delete = CTkButton(master=frame, text="Delete", command=lambda:self.delete_post(frame_holder, title))
        delete.pack(side=tk.TOP, padx=10,pady=10)
        frame.pack(expand=False, padx=10, pady=10,ipadx=80,side=tk.LEFT)
        frame_holder.pack(expand=False, fill=tk.X, side=tk.TOP)
    #to delete a given post
    def delete_post(self, holder, title):
        print(title)
        holder.destroy()

    