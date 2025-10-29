from os import system
from time import sleep
from file import File
from folder import Folder

def main_menu():
    while True:
        system("clear")
        print("LAB 10 - Main Menu")
        print("\t1. File management")
        print("\t2. Folders management")
        print("\t0. Exit...")

        option = int(input("Select the option: "))

        if option == 1:
            file_menu()
            #print("")
        elif option == 2: 
            folder_menu()
            #print("")
        elif option == 0:
            break
        else:
            print("Invalid option. Try again")
            sleep(2)    

def file_menu():
    while True:
        system("clear")
        print("File Menu")
        print("\t1. Open file")
        print("\t2. Write file")
        print("\t3. Update file")
        print("\t4. Copy file to a new")
        print("\t5. Delete file")
        print("\t0. Return...")

        option = int(input("Select the option: "))

        if option == 1:
            name = input("Enter the path/file name to open: ")
            f = File(name)
            f.open()
            input("Press Enter to continue...")

        elif option == 2: 
            name = input("Enter the path/file name to write: ")
            text = input("Enter the text to write: ")
            f = File(name)
            f.write(text)
            input("Press Enter to continue...")

        elif option == 3:
            name = input("Enter the path/file name to update: ")
            text = input("Enter the text to append: ")
            f = File(name)
            f.update(text)
            input("Press Enter to continue...")

        elif option == 4: 
            source = input("Enter the path/source file name: ")
            target = input("Enter the path/target file name: ")
            f = File(source)
            f.copy(target)
            input("Press Enter to continue...")

        elif option == 5:
            name = input("Enter the path/file name to delete: ")
            f = File(name)
            f.delete()
            input("Press Enter to continue...")

        elif option == 0:
            break
        else:
            print("Invalid option. Try again")
            sleep(2)  

def folder_menu():
    while True:
        system("clear")
        print("Folder Menu")
        print("\t1. Display folder content")
        print("\t2. Browse folder")
        print("\t3. Delete folder")
        print("\t0. Return...")

        option = int(input("Select the option: "))

        if option == 1:
            name = input("Enter the path/folder name to open: ")
            d = Folder(name)
            d.display()
            print("Press any key")
            input() #espera una tecla
        elif option == 2: 
            name = input("Enter the path/folder name to open: ")
            d = Folder(name)
            d.browse()
            print("Press any key")
            input() #espera una tecla
        elif option == 3:
            name = input("Enter the path/folder name to delete: ")
            d = Folder(name)
            d.delete()
            print("Press any key")
            input() #espera una tecla
        elif option == 0:
            break
        else:
            print("Invalid option. Try again")
            sleep(2)    
