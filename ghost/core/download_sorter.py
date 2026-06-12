''' PROJECT: Automate folder sorting with python '''
from pathlib import Path
from colorama import *
import os, shutil
import sys
import time
import random

# Global varibles
init()

def progress_bar(current, total, filename):
    width = 20
    progress = int((current / total)*width)

    bar = "█" * progress + '░' * (width - progress)
    percent = int((current / total) * 100)


    print(f"\r[{bar}] {percent}% | {filename[:20]}", end ="", flush = True)


# Define sorrting rules

CATEGORIES = {
    '_Images'    : ['.jpg', '.jpeg', '.png'],
    '_GIF'       : ['.gif'],
    '_Videos'    : ['.mp4', '.mkv', '.avi', '.mov'],
    '_Docs'      : ['.pdf', '.docx', '.txt'],
    '_ZIPS'      : ['.zip', '.rar', '.7z'],
    '_Installers': ['.exe', '.msi'],
    '_Code'      : ['.py', '.js', '.html', '.css', '.java', '.c', '.class', '.md'],
    '_Data'      : ['.csv', '.xlsx']
}

# Functions
def get_file_cat(filename, PATH_TO_SORT):

    if filename.startswith('_'):
        return None
    
    filepath = os.path.join(PATH_TO_SORT, filename)
    if os.path.isdir(filepath):
        return '_Folder'
    else:
        file_extension = '.' + filename.split('.')[-1]
        for cat, list_keywords in CATEGORIES.items():
            if file_extension.lower() in list_keywords:
                return cat
            
        print(Fore.RED + f'❗❕ [ ERROR ] {file_extension}:  Not Supported.   File: {filename}    Placed In: _Others' + Fore.RESET)
        return '_Others'
# Read all files

def sorter(path):
    PATH_TO_SORT = Path.home() / f'{path}'
    try:
        files = os.listdir(PATH_TO_SORT)
        total = len(files)

        for i, file in enumerate(files, 1):
            dir_name = get_file_cat(file, PATH_TO_SORT)

            if dir_name:
                dir_filepath = os.path.join(PATH_TO_SORT, dir_name)
                if not os.path.exists(dir_filepath):
                    print(Fore.YELLOW + "[ INFO ]Folder does not exist creating one.." + Fore.RESET)
                    os.makedirs(dir_filepath)
        # Move 

                old_path = PATH_TO_SORT / file
                new_path = os.path.join(PATH_TO_SORT, dir_name, file)
                try:
                    print(Fore.BLUE + f'▶ {dir_name}/{file}' + Fore.RESET)
                    shutil.move(old_path, new_path)
                except Exception as e:
                    print(Fore.RED + f'❌[ ERROR ] {dir_name} / {file} - {e}' + Fore.RESET)
            else:
                print(Fore.RED + "\n[ ERROR ]Folder already exist!" + Fore.RESET)

            progress_bar(i, total, file)
        print()

    except Exception as e:
        print(Fore.RED + f'ERROR: {e}' + Fore.RESET)


    print(Fore.GREEN + "[ INFO ] Sorting completed!" + Fore.RESET)


if __name__ == "__main__":
    sorter(input("Enter path: "))