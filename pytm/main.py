import os
import shutil
import subprocess
import platform
from pytm import functions
from pytm import print_spec
from colorama import Fore, Style, init

init(autoreset=True)

width = shutil.get_terminal_size().columns

lang = "en"

go_down_menu = ''' Chose an option: 
 up - to go up
 down - to go down'''

menu_options = {
    '1': functions.go_to_folder,
    '2': functions.new_folder,
    '3': functions.remove_folder,
    '4': lambda: functions.openfile(safe_input_menu('Give me a name: ')),
    'exit': lambda: exit()
 }


def main():
    while True:
        functions.print_line("=")
       
        print(' current folder is ' + functions.wim())
        print("-" * width)
        print(' files in curent folder is: ')
        print("-" * width)
       
        functions.list_files()
        
        print("=" * width)
        print(print_spec.menu[lang])
        print("-" * width)
      
        option = functions.safe_input_menu("choose an option: ")

        if option in menu_options:
           menu_options[option]()
        else:
            print(' Error: invalid option')


if __name__ == "__main__":
    main()


"""
wim()

path = input("give me a path: ").strip()

change_short(path)
"""
