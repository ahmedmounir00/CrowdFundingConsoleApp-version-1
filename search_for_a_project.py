import json
from create_a_project import *
import datetime
import home


def search_for_a_project():
    search_list = []
    file_path = r"E:\My_Projects\pythonPtoj\CrowdFundingConsoleApp\store\proj.txt"
    file = open(file_path, "r")
    for line in file:
        search_reader = json.loads(line)
        search_list.append(search_reader)

    user_date = input("Enter the date to search : ")

    def catch_date():
        for search_dict in search_list:
            if (
                search_dict["Start date"] == user_date
                or search_dict["End date"] == user_date
            ):
                print(search_list)
                home.home_page()
            else:
                print("*" * 60)
                print("press x to Exit")
                print("press t to try again")
                print("*" * 60)
                num = input("Enter your Choise : ")
                if num == "t":
                    print(
                        "This date does not represent a project , please try again by press t or press x to Exit "
                    )
                    search_for_a_project()
                elif num == "x":
                    break

    try:
        valid1 = datetime.datetime.strptime(user_date, "%d-%m-%Y")
        catch_date()
    except:
        print("This is invalid date foramt , please try again")
        print("*" * 60)
        print("press x to Exit")
        print("press t to try again")
        print("*" * 60)
        num = input("Enter your Choise : ")
        if num == "t":
            print(
                "This date does not represent a project , please try again by press t or press x to Exit "
            )
            search_for_a_project()
        elif num == "x":
            print("you choose to exit ♥")
