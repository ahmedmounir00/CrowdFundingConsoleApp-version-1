from Registration import *
from Login import *


print("*" * 50)
print("""[1]Registration""")
print("""[2]Login""")
print("""[3]Exit""")
print("*" * 50)


num = input("Please choose from the list =>")
if num == "1" or num == "R":
    x = reg()
    if bool(x):
        Login()
elif num == "2" or num == "L":
    Login()
elif num == "3" or num == "E":
    print("you select Exit , see you ♥")
    exit(0)
else:
    print("You enter a wrong option")
