import json
import home


def edit_a_project():
    edit_list = []
    file_path = r"E:\My_Projects\pythonPtoj\CrowdFundingConsoleApp\store\proj.txt"
    file = open(file_path, "r")
    for line in file:
        reader = json.loads(line)  # create a Python object from a string
        edit_list.append(reader)
    user_title = input("Enter your project's title : ")
    for word in edit_list:
        if word["title"] == user_title:
            print("** your project info is : **")
            print(word)

            key_name = input("Enter the field whose value you want to change : ")
            for key in word:
                if key == key_name:
                    key_value = input("Enter the new value : ")
                    word[key] = key_value

                    file = open(file_path, "w")
                    for add_dict in edit_list:
                        # wirte an obect in a JSON format to  file
                        json.dump(add_dict, file)
                        file.write("\n")
                    file.close()

                    print("***updated successfully ***")
                    home.home_page()
            else:
                print("*" * 60)
                print("press x to Exit")
                print("press t to try again")
                print("*" * 60)
                num = input("Enter your Choise : ")
                if num == "t":

                    print("key name is not valid  , try again ")
                    edit_a_project()
                elif num == "x":
                    break
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
            edit_a_project()
        elif num == "x":
            print("Exit choise")
