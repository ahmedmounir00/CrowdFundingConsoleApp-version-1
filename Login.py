from Registration import *
from home import *


def Login():
    log_email = input("write your account : ")
    log_password = input("write your Password : ")
    if log_email in email_list and log_password in pass_list:
        home_page()
