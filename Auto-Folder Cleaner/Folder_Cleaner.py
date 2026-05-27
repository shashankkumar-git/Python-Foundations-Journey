import os

target_dir = input("Please provide the path of the file to be cleaned: ")

def intialize_folder(folder_path):
    print("*"*15 ,"AUTOMATED FOLDER CLEANER ACTIVATED", "*"*15, "\n")

    if os.path.exists(folder_path):
        
        folder_items = os.listdir(folder_path)

        print(f"Total items in the folder is: {len(folder_items)}")
        print(f"The items in the file are as follows:\n", folder_items)

        folder = []
        files = []

        for items in folder_items:
            name, extension = os.path.splitext(items)
            
            if extension == "":
                folder.append(items)
            elif extension != "":
                files.append(items)

    else:
        print("The given path file doesn't exists")

intialize_folder(target_dir)