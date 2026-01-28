import os
import shutil
import subprocess
import platform
import print_spec
from colorama import Fore, Style, init

init(autoreset=True)

width = shutil.get_terminal_size().columns

def safe_input_menu(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print(print_spec.COLOR["error"] + print_spec.ICON["error"] + ": " + print_spec.errors["002"])

def wim():  # wim = where i am?
    cwd = os.getcwd()
    print(print_spec.COLOR["info"] + print_spec.small_talks_en["1"] + " " + cwd)
    return cwd

def change(path_to_go):
    if os.path.isdir(path_to_go):
        print(print_spec.COLOR["ok"] + print_spec.small_talks_en["2"] + path_to_go)
        print("=" * width)
        os.chdir(path_to_go)
        wim()
    else:
        print(print_spec.COLOR["error"] + print_spec.ICON["error"], print_spec.errors["003"])

def change_short(path_for_short):
    current_path = wim()
    full_path = os.path.join(current_path, path_for_short) #  обьединение путей через библиотеку

    if os.path.isdir(full_path):
        print(print_spec.COLOR["info"] + print_spec.small_talks_en["1"] + path_for_short)
        print("=" * width)
        os.chdir(full_path)
        wim()
    else:
        print(print_spec.COLOR["error"] + print_spec.ICON["error"] + " " + print_spec.errors["001"])

def go_up():
    print(print_spec.COLOR["ok"] + print_spec.small_talks_en["3"])
    print("=" * width)
    os.chdir('../')
    wim()
    

def go_to_folder():
    options = {
        "up": lambda: go_up(),
        "full": lambda: change(safe_input_menu(print_spec.small_talks_en["4"])),
        "short": lambda: change_short(safe_input_menu(print_spec.small_talks_en["5"])),
        "0": lambda: None  # для выхода
    }
    
    print("=" * width, print_spec.go_to_folder_menu["en"], "-" * width, sep="\n")
    
    while True:
        option = input(print_spec.small_talks_en["6"]).strip().lower()
        if option in options:
            if option == "0":
                break
            options[option]()
            break
        else:
            print(print_spec.COLOR["error"] + print_spec.ICON["error"] + print_spec.errors["004"])



def list_files():
    files = os.listdir()
    if not files:
        print(print_spec.COLOR["warn"] + print_spec.small_talks_en["7"])
    else:
        for file in files:
            print(f" {print_spec.ICON['folder']} {file}" if os.path.isdir(file) else f" {print_spec.ICON['file']} {file}")

def new_folder():
    folder_name = input(print_spec.small_talks_en["8"]).strip()
    try:
        os.makedirs(folder_name, exist_ok=True)
        print(f"Folder {folder_name} created {print_spec.ICON['ok']}")
    except Exception as error:
        print_error(error)

def remove_folder():
    folder_name = input(print_spec.small_talks_en["9"]).strip()
    if os.path.isdir(folder_name):
        try:
            os.rmdir(folder_name)
            print(f"Folder {folder_name} has been removed")
        except Exception as error:
            print_error(error)
    else:
        print_error(f"{print_spec.COLOR['error']}{print_spec.ICON['error']} {print_spec.errors['005']}")

def openfile(file_name):
    if not os.path.isfile(file_name):
        print(print_spec.COLOR["error"] + print_spec.ICON["error"] + print_spec.errors["005"])
        return

    try:
        if platform.system() == "Windows":
            os.startfile(file_name)  # Открытие в стандартном приложении (Windows)
        elif platform.system() == "Darwin":  # macOS
            subprocess.run(["open", file_name])
        else:  # Linux
            subprocess.run(["xdg-open", file_name])
        print(f"{print_spec.ICON['ok']} Opening {file_name}...")
    except Exception as e:
        print(print_spec.ICON["error"], e)



""" SECONDARY FUNCTION ----------------------------------"""

def print_line(char):
    print(char * width)

def print_error(msg):
    print(f"X Error X: {msg}")

""" ================================================= """
