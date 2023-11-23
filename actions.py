
from customtkinter import *
import tkinter as tk 
from PIL import Image
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
###################################################
########### create the home page ##################
###################################################
class LoggedIn:
    def __init__(self, parent):
        #selected item to view
        self.selected = "Home"
        self.frame_dictionary = {}
        self.menus_items = {}
        # creating the pages
        self.side_bar = CTkFrame(master=parent, fg_color="#1A0301")
        self.main_page = CTkFrame(master=parent,fg_color="white" )
        self.menus = {"Home":lambda:self.change("Home"), "Developers":lambda:self.change("Developers"), "Profile":lambda:self.change("Profile"), "Log Out":lambda:self.change("Log Out")}
        self.menus_page = {"Home":self.home_page, "Developers":self.dev_page, "Profile":self.profile_page, "Log Out":self.log_out_page}
        
        

        
        # placing the pages
        self.side_bar.pack(fill=tk.Y, side=tk.LEFT, padx=5)
        self.side_bar.configure(width=200)
        self.main_page.pack(fill=tk.BOTH, expand=True, side=tk.RIGHT, padx=5)
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
            self.frame_dictionary[frames] = CTkScrollableFrame(master=self.main_page, fg_color="white")
            if frames == self.selected:
                self.frame_dictionary[frames].pack(fill=tk.BOTH, expand=True)
        self.menus_page[self.selected](self.frame_dictionary[self.selected])
        # recreate the buttons
        #list of menu lists for now
        self.menus_items = {}
        
        for item in self.menus.keys():
            self.menus_items[item] = CTkButton(master=self.side_bar, text=item, fg_color="transparent",text_color="white", hover_color="#0088ff", command=self.menus[item],border_spacing=0)

        #self.side_bar.option_clear()
        for i in self.menus_items.keys():
            if i == self.selected:
                self.menus_items[i]._bg_color = "#0088ff"
            self.menus_items[i].pack(fill=tk.X, side=tk.TOP, pady=5, padx=5)

    ##################################################################
    ######################create page contents########################
    ##################################################################
    def home_page(self, parent):
        pass
    def dev_page(self, parent):
        pass
    def profile_page(self, parent):
        infos = {"user_age":"Age", "user_gender":"Gender", "p_lang":"Programming Language",  "organization":"Work Place"}
        inputs = {}
        for i in infos.keys():
            inputs[i] = CTkEntry(master=parent, placeholder_text=infos[i])
            inputs[i].pack(ipadx=50,ipady=5,padx=10,pady=10,expand=False, side=tk.TOP)
        warning = CTkLabel(master=parent, text="If You have already entered your info before know that it will be overwritten", text_color="red")
        warning.pack(side=tk.TOP, pady=10)
        add_info = CTkButton(master=parent, text="Update/Enter", command=lambda:self.update_info(inputs))
        add_info.pack(side=tk.TOP, pady=10)
    def log_out_page(self, parent):
        warning = CTkLabel(master=parent, text="Are you sure you wanna log out!", text_color="red")
        warning.pack(side=tk.TOP, pady=10)
        yes = CTkButton(master=parent, text="YES", fg_color="#170A17", command=self.log_out)
        yes.pack(side=tk.TOP, pady=10)
        no = CTkButton(master=parent, text="No", fg_color="#170A17", command=lambda:self.change("Home"))
        no.pack(side=tk.TOP, pady=10)
    def log_out(self):
        pass
    def update_info(self, inputs):
        pass
    def single_dev(self, parent, name, user_name,  url="dev_icon.png"):
        frame_holder = CTkFrame(master=parent, fg_color="transparent")
        frame = CTkFrame(master=frame_holder,fg_color="#170A17")
        frame_info = CTkFrame(master=frame, fg_color="transparent")
        
        name = CTkLabel(master=frame_info, text=name, font=("Normal", 12), text_color="white")
        user_name = CTkLabel(master=frame_info, text="@"+user_name, font=("Normal", 12), text_color="white")
        name.pack(expand=False, padx=5, pady=5, side=tk.TOP)
        user_name.pack(expand=False, padx=5, pady=5, side=tk.TOP)
        img = CTkImage(light_image=Image.open(url), size=(40,40))
        img_= CTkLabel(master=frame, image=img, text="")
        img_.pack(expand=False, side=tk.LEFT, padx=10)

        frame.pack(expand=False, side=tk.LEFT, fill=tk.X, ipadx=10)
        frame_info.pack(expand=False, side=tk.LEFT)
        frame_holder.pack(expand=False, padx=10, pady = 10, side=tk.TOP, fill=tk.X)


    def single_post(self, parent,title="", message="", url=""):
        #check if the image actually exists
        file_exist = os.path.exists(url)
        #create a page to display all posted ifos
        frame_holder = CTkFrame(master=parent, fg_color="transparent",bg_color="transparent")
        frame = CTkFrame(master=frame_holder, fg_color="#170A17", corner_radius=10,bg_color="transparent")
        frames_to_dis = [CTkFrame(master=frame, fg_color="transparent",bg_color="transparent") for i in range(3)]
        t_text = CTkLabel(master=frames_to_dis[0], text=title, text_color="white",bg_color="transparent",font=("Bold", 15))
        t_text.pack(padx=10,expand=False, side=LEFT)
        m_text = CTkLabel(master=frames_to_dis[1], text=message, text_color="white",bg_color="transparent",font=("Normal", 10), justify=tk.LEFT)
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
        