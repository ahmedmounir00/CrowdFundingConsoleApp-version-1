# from Login import *

email_list = []
pass_list = []


def reg():
    global email_list
    global pass_list
    fname = input("Please type your first Name => ")
    lname = input("Please type your Last Name => ")
    email = input("Please type your Email ex: am@gmail.com => ")
    password = input("Please type your Password => ")
    con_password = input("Please type your Password again => ")
    mobile_phone = input("Please type your Phone ex: 01010693543 => ")

    def email_validation():
        if "@" in email and "." in email[-1:-5:-1]:
            email_list.append(email)
        else:
            raise Exception("error from email")

    def pass_validation():
        if password == con_password:
            pass_list.append(password)
        else:
            raise Exception("error from pass")

    def phone_validation():
        if (
            len(mobile_phone) == 11
            and mobile_phone.startswith("01")
            and mobile_phone.isdigit()
        ):
            print("11111")

        else:
            raise Exception("error from phone")

    try:
        pass_validation()
        phone_validation()
        email_validation()
        print("before login")
        # print(email_list)
        # Login(email_list, pass_list)
        return True
    except ValueError:
        print(ValueError)
        return False
