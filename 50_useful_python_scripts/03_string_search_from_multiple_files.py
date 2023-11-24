"""
Find a file with the supplied string in the folder of your choosing
"""

import os

text = input("Input text: ")
path = input("Input path: ")


# os.chdir(path)

def getfiles(path):
    f = 0
    os.chdir(path)
    files = os.listdir()
    # print(files)
    for file_name in files:
        abs_path = os.path.abspath(file_name)
        if os.path.isfile(abs_path):
            getfiles(abs_path)
        if os.path.isfile(abs_path):
            f = open(file_name, "r")
            if text in f.read():
                f = 1
                print(text + "Found in ")
                final_path = os.path.abspath(file_name)
                print(final_path)
                return True
    if f == 1:
        print(text + "Not found!")
        return False


getfiles(path)
