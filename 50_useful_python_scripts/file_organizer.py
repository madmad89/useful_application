# File organizer

# Input data:
#     - Path to folder
# Const:
#     - DIR_NAMES
#     - FILE EXTENSION
#
# OUTPUT:
#     - Move files in the specific folder


import os
import shutil


def menu():
    # Prompts the user to input a path or press 'Q' to exit the program
    path = input('Insert the path or press Q to exit the program: ')
    while not path_validation(path):
        if path == 'Q':
            exit()
        path = input('Insert the path or press Q to exit the program: ')
    print('The path is valid')
    return path


def path_validation(path: str) -> bool:
    # Checks if the given path is a valid directory
    return os.path.isdir(path)


def create_dirs(path: str):
    # Creates directories within the specified path based on predefined directory names
    for dir in DIR_TYPES:
        if not os.path.isdir(path + '\\' + dir):
            os.mkdir(path + '\\' + dir)


def list_all_files(path: str) -> list:
    # Lists all files in the specified directory
    files = [file for file in os.listdir(path) if os.path.isfile(path + '\\' + file)]
    return files


def extract_file_extension(file: str) -> str:
    # Extracts the file extension from the given filename
    filename, extension = os.path.splitext(file)
    return extension


def map_extension_to_folder(path: str) -> dict:
    # Maps file extensions to directories based on the given path
    # indexes = [i for i, ch in enumerate(file) if ch == '.']
    # if indexes:
    #     file_extension = file[indexes[-1]::]
    #     return file_extension
    # else:
    #     return 'no extension'
    # # varianta 2 #
    # index = file.rfind('.')
    # print(index)
    # if index != -1:
    #     return file[index::]
    # else:
    #     return 'no extension'

    # # varianta 3 #
    extension_mapping = {path + '\\' + dir: FILE_EXT_TYPES[i] for i, dir in enumerate(DIR_TYPES)}
    return extension_mapping


if __name__ == '__main__':
    # Predefined directory names
    DIR_TYPES = ['Pictures', 'Videos', 'PDF_files',
                 'Music', 'TXT_files', 'Python_files',
                 'Word_files', 'Excel_files', 'Exe_files',
                 'Archived_files', 'CDR_files'
                 ]

    # Predefined file extension types
    FILE_EXT_TYPES = [['.jpg', '.jpeg', '.png', '.JPG'], ['.mp4', 'MP4', '.mov', '.MOV', '.avi'], ['.pdf', '.PDF'],
                      '.mp3', '.txt', '.py',
                      ['.doc', '.docx'], ['.csv', '.xlsx', 'xls'], '.exe',
                      ['.7z', '.zip'], '.cdr'
                      ]

    # Prompt for a valid path and perform file organization
    path = menu()
    mapping = map_extension_to_folder(path)
    # print(mapping)
    create_dirs(path)
    files = list_all_files(path)
    # print(files)
    for file in files:
        file_extension = extract_file_extension(file)
        # print(file_extension)
        for k, v in mapping.items():
            if file_extension in v:
                try:
                    shutil.move(path + '\\' + file, k)
                except:
                    print(file + ' cannot be moved!')
