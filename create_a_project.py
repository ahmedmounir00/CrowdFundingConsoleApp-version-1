import home
from datetime import *
import json


def create_a_project():
    title = input("Enter your proj title => ")
    Details = input("Enter your proj details => ")
    total_target = int(input("Enter your total target , should be an integer num => "))
    start_date = input("""Enter Start date , should be "dd-mm-yyyy" => """)
    end_date = input("""Enter End date , should be "dd-mm-yyyy" => """)
    mydict = {
        "title": title,
        "details": Details,
        "total target": total_target,
        "Start date": start_date,
        "End date": end_date,
    }
    file_path = r"E:\My_Projects\pythonPtoj\CrowdFundingConsoleApp\store\proj.txt"

    def file_store():
        file = open(file_path, "a")
        file.write(
            json.dumps(mydict)
        )  # use dumps() to get a JSON string from an object
        file.write("\n")
        file = open(file_path, "r")
        for line in file:
            print(line)

    try:
        valid1 = datetime.strptime(start_date, "%d-%m-%Y")
        valid1 = datetime.strptime(end_date, "%d-%m-%Y")
        file_store()
        home.home_page()
    except ValueError:
        print("you entered incorrect date format")
        print(mydict)
