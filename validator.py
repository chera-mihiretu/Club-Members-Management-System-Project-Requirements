
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
def user_name_validator(text):
    if len(text) < 6:
        raise ValidationError("Short user name")
    if not (text.find("#") == -1) or not (text.find("@") == -1):
        raise ValidationError("User name cannot contain '#' or '@' ")
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
class DatabaseError(Exception):
    def __init__(self, message):
        self.message = message
