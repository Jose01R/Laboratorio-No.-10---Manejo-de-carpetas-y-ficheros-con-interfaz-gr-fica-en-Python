
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path

#DEFINIMOS VAR GLOBALES
file_path = None
home_dir = Path.home()
initial_dir = home_dir / "Documents"


def open_file(window, entry, textArea, buttons):
    global file_path, initial_dir

    #abre el cuadro de dialogo para seleccionar el archivo
    file_path = filedialog.askopenfilename(parent=window, initialdir=initial_dir, title="Select the file", filetypes=[('Text Files', '*.txt')])

    if file_path:
        #leer el contenido
        with open(file_path, 'r') as file:
            file_content = file.read()

            """
            si se selecciona un archivo se debe actualizar 
            el entry (campo de texto) y el scrolledText
            """
            entry.config(state="normal")
            entry.delete(0, tk.END)
            entry.insert(0, file_path)
            entry.config(state="disabled")
            textArea.delete(1.0, tk.END)
            textArea.insert(tk.INSERT, file_content)