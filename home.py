from create_a_project import *
from view_all_projects import *
from edit_on_the_project import *
from search_for_a_project import *
from delete_projects import *


def home_page():
    print("*" * 50)
    print("""[1]Create a prject : """)
    print("""[2]Veiw All project : """)
    print("""[3]Edit own project : """)
    print("""[4]Search for a Project : """)
    print("""[5]Delete a project : """)
    print("""press x to Exit : """)
    print("*" * 50)
    no = input("Please choose from the list =>")
    if no == "1":
        create_a_project()
    elif no == "2":
        view_all_projects()
    elif no == "3":
        edit_a_project()
    elif no == "4":
        search_for_a_project()
    elif no == "5":
        delete_his_own_projects()
    elif no == "x":
        print("you choose Exit")
        exit(0)
