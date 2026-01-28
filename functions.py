import os
import shutil
import subprocess
import platform
import functions



width = shutil.get_terminal_size().columns

def safe_input_menu(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("❌ Empty input. Try again")

def wim():
    cwd = os.getcwd()
    print("U are in: ", cwd)
    return cwd

def change(path_to_go):
    if os.path.isdir(path_to_go):
        print("u are go to: ", path_to_go)
        print("=" * width)
        os.chdir(path_to_go)
        wim()
    else:
        print("Error 001: Not valid directory")

def change_short(path_for_short):
    current_path = wim()
    full_path = os.path.join(current_path, path_for_short) #  обьединение путей через библиотеку

    if os.path.isdir(full_path):
        print("u are go to: ", path_for_short)
        print("=" * width)
        os.chdir(full_path)
        wim()
    else:
        print("Error 001: Not valid directory")

def go_up():
    print("go up for 1 directory ")
    print("=" * width)
    os.chdir('../')
    wim()
    

def go_to_folder():
    go_to_menu = ''' Chose an option:
     up - to go up for one folder
     full - for full path
     short - for short path
     0 - to go back'''

    print("=" * width)
    print(go_to_menu)
    print("-" * width)
    
    option = input("Choose an option: ")
    option_list = {
        "up": lambda: go_up(),
        "full": lambda: change(input("Enter full path to go: ")),
        "short": lambda: change_short(input("Enter full path to go: ")),
    }




def list_files():
    files = os.listdir()
    if not files:
        print(' Folder is empty')
    else:
        for file in files:
            print(f"📂 {file}" if os.path.isdir(file) else f"📄 {file}")

def new_folder():
    folder_name = input('Enter new folder name: ').strip()
    try:
        os.makedirs(folder_name, exist_ok=True)
        print(f"Folder {folder_name} created ✅")
    except Exception as error:
        print_error(error)

def remove_folder():
    folder_name = input(" Enter folder name to remove: ").strip()
    if os.path.isdir(folder_name):
        try:
            os.rmdir(folder_name)
            print(f"Folder {folder_name} has been removed 🗑️")
        except Exception as error:
            print_error(error)
    else:
        print_error(" Folder does not exist")

def openfile(file_name):
    if not os.path.isfile(file_name):
        print("❌ Error: File does not exist")
        return

    try:
        if platform.system() == "Windows":
            os.startfile(file_name)  # Открытие в стандартном приложении (Windows)
        elif platform.system() == "Darwin":  # macOS
            subprocess.run(["open", file_name])
        else:  # Linux
            subprocess.run(["xdg-open", file_name])
        print(f"📂 Opening {file_name}...")
    except Exception as e:
        print(f"❌ Error: {e}")



""" SECONDARY FUNCTION ----------------------------------"""

def print_line(char):
    print(char * width)

def print_error(msg):
    print(f" 🚨 Error: {msg}")

""" ================================================= """
