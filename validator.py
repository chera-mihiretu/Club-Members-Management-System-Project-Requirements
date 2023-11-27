from tkinter import messagebox
def email_validator(text):
    if text == "":
        raise ValidationError("Empty Entry for email")
    if len(text) < 6:
        raise ValidationError("Very short email")
    if text.find("@") == -1:
        raise ValidationError("Invalid email adress")
    if text[text.find("@"):].find(".")==-1:
        raise ValidationError("Invalid email adress")
    if not (text.find(" ") == -1):
        raise ValidationError("Invalid email adress")

    return True
def name_validator(text):
    if len(text) < 6:
        raise ValidationError("Short name")
    if len(text) > 30:
        raise ValidationError("Too long name")
def user_name_validator(text):
    if text == "":
        raise ValidationError("Empty User name")
    if len(text) < 6:
        raise ValidationError("Short user name")
    if len(text) > 30:
        raise ValidationError("Too long user name")
    if not (text.find("#") == -1) or not (text.find("@") == -1):
        raise ValidationError("User name cannot contain '#' or '@' ")
    if not (text.find(" ") == -1):
        raise ValidationError("User name cannot contain space")
def six_less_validator(text, type_t):
    if text == "":
        raise ValidationError("Empty Entry for "+type_t)
    if len(text) < 6:
        raise ValidationError("Short input for "+type_t)


def ten_less_validator(text, type_t):
    if text == "":
        raise ValidationError("Empty Entry for "+type)
    if len(text) < 10:
        raise ValidationError("Short input for "+type_t)

class ValidationError(Exception):
    def __init__(self, message):
        self.message = message
    def display(self):
        messagebox.showerror(title="ERROR", message=self.message)

class DatabaseError(Exception):
    def __init__(self, message):
        self.message = message
    def display(self):
        messagebox.showinfo(title="ERROR", message=self.message)


## this function helps me to make the text description 
## line by line instead of a single line
def short(text):
    mode = 0
    edited_string  = ""
        
    for i in range(len(text)):
        if not i % 50 and i != 0:
            edited_string += text[mode*50:i] +"\n"
            mode +=1
    else:
        if not len(text) % 50 == 0:
            edited_string += text[mode*50:len(text)] +"\n"
    return edited_string