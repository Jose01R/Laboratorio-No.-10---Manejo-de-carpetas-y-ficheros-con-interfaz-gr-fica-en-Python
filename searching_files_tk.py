import tkinter as tk
from tkinter import filedialog, messagebox
import os
import fnmatch

#seleccionar una folder y actualizar el Entry
def select_folder(parent_window, folder_path_entry):
    
    folder = filedialog.askdirectory(parent=parent_window, title="Select Base Folder")
    if folder:
        #el Entry debe ser normal para escribir y luego readonly
        folder_path_entry.config(state="normal")
        folder_path_entry.delete(0, tk.END)
        folder_path_entry.insert(0, folder)
        folder_path_entry.config(state="readonly")

#para busqueda de archivos
def search_files(parent_window, folder_path_entry, pattern_entry, results_box):
    base_folder = folder_path_entry.get()
    pattern = pattern_entry.get().strip()
    
    if not base_folder or not pattern:
        messagebox.showwarning(parent=parent_window, title="Missing Data", message="Please select a folder and enter a search pattern.")
        return
    
    # caja de resultados para escribir
    results_box.config(state=tk.NORMAL)
    results_box.delete("1.0", tk.END)
    results_box.insert(tk.END, f"Starting searching in: {base_folder}\n")
    results_box.insert(tk.END, f"Pattern: {pattern}\n\n")
    
    found_files = []
    
    try:
        # recorre el directorio de forma recursiva
        for root_dir, dirs, files in os.walk(base_folder):
            # fnmatch.filter aplica  pattern (como *.txt) a la lista de archivos
            for filename in fnmatch.filter(files, pattern):
                found_files.append(os.path.join(root_dir, filename))
        
        if found_files:
            for f in found_files:
                results_box.insert(tk.END, f + "\n")
        else:
            results_box.insert(tk.END, "No files found.\n")

        messagebox.showinfo(parent=parent_window, title="Search Complete", message=f"found {len(found_files)} file(s).")
        
    except Exception as e:
        results_box.insert(tk.END, f"\nERROR: Could not perform search {e}")
        messagebox.showerror(parent=parent_window, title="Error", message=f"An error occurred: {e}")

    # Deshabilitar caja de resultados
    results_box.config(state=tk.DISABLED)

#limpiar la pantalla
def clear_text(folder_path_entry, pattern_entry, results_box):
    #impiar resultados (txt area)
    results_box.config(state=tk.NORMAL)
    results_box.delete("1.0", tk.END)
    results_box.config(state=tk.DISABLED)
    
    #Limpiar ptron de busq
    pattern_entry.delete(0, tk.END)
    
    #Limpiamos carpeta base
    folder_path_entry.config(state="normal")
    folder_path_entry.delete(0, tk.END)
    folder_path_entry.config(state="readonly")
