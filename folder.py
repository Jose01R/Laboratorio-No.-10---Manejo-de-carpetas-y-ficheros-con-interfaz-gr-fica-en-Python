import os 
from os import walk

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



