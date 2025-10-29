import os 
import shutil 
import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path
from os import walk 
from tkinter import simpledialog

def open_folder(parent_window, file_name_entry, text_area, buttons):
    # Abre el dialogo para seleccionar una carpeta
    # El resultado es la ruta de la carpeta seleccionada (string) o una cadena vacia si se cancela
    folder_path = filedialog.askdirectory(parent=parent_window, title="Select a folder")

    if folder_path:
        # Habilita y actualiza el campo de la ruta (Entry)
        file_name_entry.config(state="normal")
        file_name_entry.delete(0, 'end')
        file_name_entry.insert(0, folder_path)
        file_name_entry.config(state="disabled")

        # Muestra el contenido de la carpeta en el ScrolledText
        text_area.delete('1.0', 'end')  # Limpiar el area de texto
        
        try:
            #obtener el contenido del directorio
            # next(walk(...)) solo obtiene el contenido del directorio actual (sin recursion)
            current_dir, sub_dirs, files = next(walk(folder_path))

            output = f"Selected folder:\n{current_dir}\n\n"
            
            output += "Subdirectories:\n"
            if sub_dirs:
                for sub_dir in sub_dirs:
                    output += f"  - {sub_dir}\n"
            else:
                output += "  (No subdirectories)\n"

            output += "\nFiles:\n"
            if files:
                for file in files:
                    output += f"  - {file}\n"
            else:
                output += "  (No files)\n"

            text_area.insert('1.0', output)
            
            #habilitar los botones que dependen de carpeta seleccionada
            for btn in buttons:
                btn.config(state="normal")

        except Exception as e:
            error_message = f"ERROR trying to display the directory content:\n{e}"
            text_area.insert('1.0', error_message)
            
            # Deshabilitar botones en caso de error
            for btn in buttons:
                btn.config(state="disabled")

    else:
        #Si se cancela la seleccion, el area de texto limpia
        # o mensaje de cancelacion
        text_area.delete('1.0', 'end')
        text_area.insert('1.0', "Folder selection cancelled")
        
        
def browse_folder(parent_window, file_name_entry, text_area, buttons):
    # abrir el dialogo para seleccionar una carpeta
    folder_path = filedialog.askdirectory(parent=parent_window, title="Select folder to scan")

    if folder_path:
        #actualizar el Entry con la ruta seleccionada
        file_name_entry.config(state="normal")
        file_name_entry.delete(0, 'end')
        file_name_entry.insert(0, folder_path)
        file_name_entry.config(state="disabled")

        # lmpiar el area de texto e iniciar el recorrido recursivo
        text_area.delete('1.0', 'end')
        output = f"Starting recursive scan in:\n**{folder_path}**\n\n"
        separator = "-" * 40 + "\n"
        
        try:
            for root, dirs, files in os.walk(folder_path):
                # Generar una indentacion para visualizar mejor la profundidad
                level = root.replace(folder_path, '').count(os.sep)
                indent = ' ' * 4 * level
                
                # Nombre del directorio actual
                output += f"{indent}Directory: **{os.path.basename(root) if root != folder_path else folder_path}**\n"
                
                # Subdirectorios
                if dirs:
                    output += f"{indent}    ∟ Subdirectories: {', '.join(dirs)}\n"

                # Archivos
                if files:
                    output += f"{indent}    ∟ Files:    {', '.join(files)}\n"

            #Insertar la salida en el ScrolledText
            text_area.insert('1.0', output)
            
            #habilitar botones de control 
            for btn in buttons:
                btn.config(state="normal")
                
        except Exception as e:
            #Manejo de errores
            error_message = f"ERROR while traversing the directory:\n{e}"
            text_area.insert('1.0', error_message)
            messagebox.showerror("Scan Error", error_message)
            
            #deshabilitar botones 
            for btn in buttons:
                btn.config(state="disabled")

    else:
        # Si la seleccion es cancelada
        text_area.delete('1.0', 'end')
        text_area.insert('1.0', "Folder scan cancelled")

def clear(parent_window, file_name_entry, text_area, buttons):
    
    # Limpiar el Entry (Campo de la ruta)
    # Es necesario habilitarlo primero para poder modificar su contenido
    file_name_entry.config(state="normal")
    file_name_entry.delete(0, 'end')
    file_name_entry.config(state="disabled") # Devolver al estado original

    # Limpiar el ScrolledText (Area de contenido)
    text_area.delete('1.0', 'end')
    text_area.insert('1.0', "Folder manager reset")

    # Deshabilitar los Botones Controlados
    # La lista 'buttons' contiene [saveAsBtn, deleteBtn]
    for btn in buttons:
        btn.config(state="disabled")
     
def delete_folder(parent_window, file_name_entry, text_area, buttons):
    
    # Obtener la ruta del folder desde el Entry
    # Primero, deshabilitamos el estado para poder leer el contenido
    file_name_entry.config(state="normal")
    folder_path = file_name_entry.get().strip()
    file_name_entry.config(state="disabled") # Volvemos a deshabilitar

    # Limpiar el area de texto antes de empezar
    text_area.delete('1.0', 'end') 

    # SE VERIFICA EXISTENCIA DEL FOLDER
    if not folder_path:
        text_area.insert('1.0', "ERROR: No folder path selected")
        messagebox.showerror("Error", "You must select a folder first")
        return
        
    if not os.path.isdir(folder_path):
        text_area.insert('1.0', f"ERROR: The folder '{folder_path}' does not exist")
        messagebox.showerror("Error", f"The folder '{folder_path}' does not exist")
        return

    # VERIFICAMOS SI EL USER QUIERE REALMENTE BORRAR 
    confirmation = messagebox.askyesno(
        "Confirm Deletion",
        f"Do you really want to delete the folder '{folder_path}' and ALL its contents?\n\nThis action is irreversible!",
        icon='warning',
        parent=parent_window # Para que el dialogo este sobre la ventana hija
    )

    if confirmation: # confirmation es True si el usuario selecciona 'Si'
        try:
            # BORRAMOS FOLDER Y CONTENIDO RECURSIVAMENTE
            shutil.rmtree(folder_path)
            
            # Exito: Actualizar la GUI
            text_area.insert('1.0', f"Folder '{folder_path}' and its contents were successfully deleted")
            
            # Limpiar el Entry
            file_name_entry.config(state="normal")
            file_name_entry.delete(0, 'end')
            file_name_entry.config(state="disabled")

            # Deshabilitar botones que dependen de carpeta existente
            for btn in buttons:
                btn.config(state="disabled")
            
        except Exception as e:
            # Manejo de errores 
            error_msg = f"ERROR deleting folder '{folder_path}': {e}"
            text_area.insert('1.0', error_msg)
            messagebox.showerror("Deletion Error", error_msg)
    
    else: # El usuario selecciona 'No'
        text_area.insert('1.0', f"Cancelled: Deletion of folder '{folder_path}' was cancelled by the user")

def save_folder_as(parent_window, file_name_entry, text_area, buttons):
    
    # Abre el dialog para que el user elija  ruta y  nombre de la NUEVA carpeta
    # Usamos askdirectory. El usuario debe crear o seleccionar la carpeta de destino
    new_folder_path = filedialog.askdirectory(
        parent=parent_window, 
        title="Select the Location for the New Folder"
    )

    if new_folder_path:
        # askdirectory dialog devuelve ruta seleccionada

        # Pedimos al usuario el nombre que quiere darle a la nueva carpeta
        new_folder_name = simpledialog.askstring("Folder Name", "Enter the name of the new folder:")
        
        if new_folder_name:
            # Construimos la ruta completa de la nueva carpeta
            final_path = os.path.join(new_folder_path, new_folder_name)
            
            # limpiamos text area
            text_area.delete('1.0', 'end')
            
            try:
                # makedirs para crear directorios si no existe
                os.makedirs(final_path, exist_ok=True) 
                
                output = f"Folder successfully created in:\n{final_path}"
                text_area.insert('1.0', output)
                
                #actualizamos entry con nuevo path
                file_name_entry.config(state="normal")
                file_name_entry.delete(0, 'end')
                file_name_entry.insert(0, final_path)
                file_name_entry.config(state="disabled")

                # Habilitar botones
                for btn in buttons:
                    btn.config(state="normal")
                
            except Exception as e:
                error_msg = f"ERROR trying to create the folder:\n{e}"
                text_area.insert('1.0', error_msg)
                messagebox.showerror("Creation Error", error_msg)
        
        else:
            text_area.delete('1.0', 'end')
            text_area.insert('1.0', "Folder creation cancelled (no name provided)")

    else:
        # Si se cancela la seleccin de ubicacin
        text_area.delete('1.0', 'end')
        text_area.insert('1.0', "Save as cancelled (no location selected)")