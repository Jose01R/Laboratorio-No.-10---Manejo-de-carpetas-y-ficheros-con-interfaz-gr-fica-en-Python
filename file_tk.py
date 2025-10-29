
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path
from file import File  # Tu clase File

# Variables globales
file_path = None
home_dir = Path.home()
initial_dir = home_dir / "Documents"


def open_file(window, entry, textArea):
    global file_path, initial_dir
    file_path = filedialog.askopenfilename(
        parent=window,
        initialdir=initial_dir,
        title="Select a file",
        filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')]
    )
    if file_path:
        f = File(file_path)
        f.open()  # Muestra contenido en consola

        # Mostrar contenido en el textArea
        with open(file_path, 'r') as file_obj:
            content = file_obj.read()

        entry.config(state="normal")
        entry.delete(0, tk.END)
        entry.insert(0, file_path)
        entry.config(state="disabled")

        textArea.delete(1.0, tk.END)
        textArea.insert(tk.INSERT, content)


def save_file(window, entry, textArea):
    global file_path
    if not file_path:
        messagebox.showwarning("Warning", "No file selected. Use 'Save As' instead.", parent=window)
        return
    content = textArea.get(1.0, tk.END)
    f = File(file_path)
    f.write(content)
    messagebox.showinfo("Success", f"File saved:\n{file_path}", parent=window)


def save_as_file(window, entry, textArea):
    global file_path, initial_dir
    new_path = filedialog.asksaveasfilename(
        parent=window,
        initialdir=initial_dir,
        title="Save file as",
        defaultextension=".txt",
        filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')]
    )
    if new_path:
        content = textArea.get(1.0, tk.END)
        f = File(new_path)
        f.write(content)

        file_path = new_path
        entry.config(state="normal")
        entry.delete(0, tk.END)
        entry.insert(0, file_path)
        entry.config(state="disabled")

        messagebox.showinfo("Success", f"File saved as:\n{file_path}", parent=window)


def delete_file(window, entry, textArea):
    global file_path
    if not file_path:
        messagebox.showwarning("Warning", "No file selected to delete.", parent=window)
        return
    f = File(file_path)
    if messagebox.askyesno("Confirm", f"Do you really want to delete:\n{file_path}?", parent=window):
        f.delete()
        entry.config(state="normal")
        entry.delete(0, tk.END)
        entry.config(state="disabled")
        textArea.delete(1.0, tk.END)
        file_path = None
        messagebox.showinfo("Deleted", "File deleted successfully.", parent=window)


def clear_text(entry, textArea):
    textArea.delete(1.0, tk.END)
    entry.config(state="normal")
    entry.delete(0, tk.END)
    entry.config(state="disabled")

