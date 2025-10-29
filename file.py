import os

class File:
    def __init__(self, name):
        self.name = name

    # a. Abrir y mostrar el contenido
    def open(self):
        try:
            with open(self.name, "r") as f:
                content = f.read()
                print("\n--- File content ---")
                print(content)
                print("--------------------")
        except Exception as e:
            print(f"ERROR: {e} trying to open file: {self.name}")

    # b. Crear o sobrescribir archivo
    def write(self, characters):
        try:
            with open(self.name, "w") as f:
                f.write(characters)
                print(f"Data successfully written to {self.name}")
        except Exception as e:
            print(f"ERROR: {e} trying to write to file: {self.name}")

    # c. Actualizar/agregar contenido al final
    def update(self, characters):
        try:
            with open(self.name, "a+") as f:  # a+ para leer/escribir agregando
                f.write(characters)
                print(f"Data successfully appended to {self.name}")
        except Exception as e:
            print(f"ERROR: {e} trying to update file: {self.name}")

    # d. Copiar el contenido a otro archivo
    def copy(self, target):
        try:
            with open(self.name, "r") as src:
                data = src.read()
            with open(target, "w") as dest:
                dest.write(data)
            print(f"File successfully copied to {target}")
        except Exception as e:
            print(f"ERROR: {e} trying to copy file: {self.name}")

    # e. Eliminar el archivo
    def delete(self):
        try:
            if os.path.exists(self.name):
                os.remove(self.name)
                print(f"File {self.name} deleted successfully.")
            else:
                print(f"File {self.name} does not exist.")
        except Exception as e:
            print(f"ERROR: {e} trying to delete file: {self.name}")
