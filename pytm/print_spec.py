from colorama import Fore, Style, init

init(autoreset=True)

COLOR = {
    "ok": Fore.GREEN,
    "error": Fore.RED,
    "warn": Fore.YELLOW,
    "info": Fore.CYAN,
    "reset": Style.RESET_ALL
}

ICON = {
    "ok": "[+]",
    "error": "[X]",
    "warning": "[!]",
    "folder": "|  folder  |",
    "file": "|  file    |"
}

errors = {
    "001": "Error: Not valid directory",
    "002": "Empty input. Try again",
    "003": ": No valid directory",
    "004": "Invalid option",
    "005": ": Folder does not exist"
}

small_talks_en = {
    "1": "U are in: ",
    "2": "u are go to: ",
    "3": "go up for 1 folder",
    "4": "Enter full path to go: ",
    "5": "Enter relative path to go: ",
    "6": "Choose an option: ",
    "7": "Folder is empty",
    "8": "Enter new folder name: ",
    "9": "Enter folder name to remove: "
}

menu = {
	"en": '''\
|    1      | - go to a folder 
|    2      | - make a folder 
|    3      | - remove a folder
|    4      | - open file
|    exit   | - to exit
    ''',

    "ru": '''\
|    1      | - перейти в папку
|    2      | - создать папку
|    3      | - удалить папку
|    4      | - открыть файл
|    exit   | - выйти из программы
    ''',
    
    "cz": '''\
|    1      | - přejít do složky
|    2      | - vytvořit složku
|    3      | - odstranit složku
|    4      | - otevřít soubor
|    exit   | - ukončit program
    ''',
    
}

go_to_folder_menu = {
    "en": '''\
Chose an option:
     up - to go up for one folder
     full - for full path
     short - for short path
     0 - to go back
     ''',
     
     "ru": '''\
Выберите один из вариантов:
     up — перейти на один уровень вверх по папке
     full — полный путь
     short — короткий путь
     0 — вернуться назад
     ''',
     
     "cz": '''\
Vyberte možnost:
     up – pro přechod o jednu složku výše
     full – pro úplnou cestu
     short – pro zkrácenou cestu
     0 – pro návrat zpět
     '''
}
