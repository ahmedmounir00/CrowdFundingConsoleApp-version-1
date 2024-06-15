import json
from create_a_project import *
import home


def view_all_projects():
    view_list = []
    file_path = r"E:\My_Projects\pythonPtoj\CrowdFundingConsoleApp\store\proj.txt"
    file = open(file_path, "r")
    for line in file:
        view_dict = json.loads(line)  # create a Python object from a string
        view_list.append(view_dict)

    print(view_list)
    home.home_page()
