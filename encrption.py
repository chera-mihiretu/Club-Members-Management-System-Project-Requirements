##############################################
#this class will help for password encryption#
##############################################
import bcrypt
salt = b'$2b$05$vB9qsaEoyUS.anNRk1yeX.'
def hash_it(password):
    password = password.encode()
    return bcrypt.hashpw(password, salt)
def check_equal(password, pre_hash):
    password = password.encode()
    hashed_pwd = bcrypt.hashpw(password, salt)
    if hashed_pwd == pre_hash:
        return True
    return False
