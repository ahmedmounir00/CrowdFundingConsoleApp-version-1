import json
from create_a_project import *
import home


def delete_his_own_projects():
    delete_list = []
    file_path = r"E:\My_Projects\pythonPtoj\CrowdFundingConsoleApp\store\proj.txt"
    # show the projects from the file
    file = open(file_path, "r")
    for line in file:
        reader_del = json.loads(line)
        delete_list.append(reader_del)

    # search for the project
    user_proj_name = input("please enter your title : ")
    for dict_in_list in delete_list:
        # if title of the proj in our list it will be remove this dict
        if dict_in_list["title"] == user_proj_name:
            delete_list.remove(dict_in_list)

            # update in the JSON file
            file = open(file_path, "w")
            # it will be loop on the deleted list contant
            for add in delete_list:
                # and add python obect in a JSON format to a file
                json.dump(add, file)
                file.write("\n")
            print("***project deleted successfully***")
            file.close()
            home.home_page()
        else:
            continue
    else:
        print("*" * 60)
        print("press x to Exit")
        print("press t to try again")
        print("*" * 60)
        num = input("Enter your Choise : ")
        if num == "t":
            print("this project is not in the store , try again ")
            delete_his_own_projects()
        elif num == "x":
            print("Exit choise")
