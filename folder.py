import os 
from os import walk
import shutil # para eliminacion recursiva

class Folder():

    def __init__(self, name):
        self.name = name

    def display(self):
        # MUESTRA CONTENIDO DE LA CARPETA ACTUAL
        try:
            current_dir, sub_dir, files = next(walk(self.name))
            print("Folder: ", current_dir)
            print("Sub folder: ", sub_dir)
            print("Files: ", files)

        except Exception as e:
            print(f"ERROR {e} trying to display directory content of the file {self.name}")  

    def browse(self):
        
        # Comprobar si el directorio existe
        if not os.path.isdir(self.name):
            print(f"ERROR: The directory '{self.name}' does not exist.")
            return

        # Recorrer el directorio y todos sus subdirectorios
        print(f"Contents of the directory '{self.name}' and subdirectories:")
        print("-" * 30)
        
        # os.walk genera una tupla (dirpath, dirnames, filenames) para cada directorio
        # en el arbol, incluyendo el directorio root
        for current_dir, sub_dirs, files in os.walk(self.name):
            print(f"Current Directory: **{current_dir}**")
            
            # Subdirectorios
            if sub_dirs:
                print(f"   ∟ SubDirs: {', '.join(sub_dirs)}")

            # Files
            if files:
                print(f"   ∟ Files:    {', '.join(files)}")

            print("-" * 30)


    def delete(self):
        
        #SE VERIFICA EXISTENCIA DEL FOLDER
        if not os.path.isdir(self.name):
            print(f"ERROR: The folder '{self.name}' does not exist.")
            return

        #VERIFICAMOS SI EL USER QUIERO REALMENTE BORRAR
        confirmation = input(
            f"Do you really want to delete the folder '{self.name}' and its content. [Y/N]: "
        ).strip().upper()

        if confirmation == 'Y':
            try:
                #BORRAMOS FOLDER Y CONTENMT
                shutil.rmtree(self.name)
                print(f"Folder '{self.name}' and its content deleted successfully.")
            
            except Exception as e:
                # 4. Error handling (e.g., permissions issues)
                print(f"ERROR trying to delete folder '{self.name}': {e}")
        
        elif confirmation == 'N':
            print(f"Deletion of folder '{self.name}' cancelled by the user.")
        
        else:
            print("Invalid input. Deletion cancelled.")

            