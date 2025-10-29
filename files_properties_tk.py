import os
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from pathlib import Path
from datetime import datetime

# Variables globales
file_path = None
home_dir = Path.home()
initial_dir = home_dir / "Documents"

def select_file(window, entry, textArea):
    global file_path
    file_path = filedialog.askopenfilename(
        parent=window,
        initialdir=initial_dir,
        title="Select a file",
        filetypes=[('All Files', '*.*')]
    )
    if file_path:
        entry.config(state="normal")
        entry.delete(0, tk.END)
        entry.insert(0, file_path)
        entry.config(state="disabled")
        show_properties(textArea)

def show_properties(textArea):
    global file_path
    if not file_path:
        return
    
    try:
        file_stats = os.stat(file_path)
        name = os.path.basename(file_path)
        full_path = os.path.abspath(file_path)
        size = file_stats.st_size
        ext = os.path.splitext(file_path)[1] or "Unknown"
        creation = datetime.fromtimestamp(file_stats.st_ctime).strftime("%Y-%m-%d %H:%M:%S")
        last_update = datetime.fromtimestamp(file_stats.st_mtime).strftime("%Y-%m-%d %H:%M:%S")
        readable = os.access(file_path, os.R_OK)
        writable = os.access(file_path, os.W_OK)
        executable = os.access(file_path, os.X_OK)
        permissions = f"{'r' if readable else '-'}{'w' if writable else '-'}{'x' if executable else '-'}"

        textArea.delete(1.0, tk.END)
        props = (
            f"Name: {name}\n"
            f"Full Path: {full_path}\n"
            f"Size: {size} bytes\n"
            f"File Type: {ext}\n"
            f"Creation Date: {creation}\n"
            f"Last Update: {last_update}\n"
            f"Permissions: {permissions}\n"
            f"Readable: {readable}\n"
            f"Writable: {writable}\n"
            f"Executable: {executable}\n"
        )
        textArea.insert(tk.INSERT, props)
    except Exception as e:
        messagebox.showerror("Error", f"Cannot get file properties:\n{e}", parent=textArea.master)

def export_properties(window, textArea):
    global file_path
    if not file_path:
        messagebox.showwarning("Warning", "No file selected.", parent=window)
        return
    save_path = filedialog.asksaveasfilename(
        parent=window,
        initialdir=initial_dir,
        title="Save properties as",
        defaultextension=".txt",
        filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')]
    )
    if save_path:
        with open(save_path, "w") as f:
            f.write(textArea.get(1.0, tk.END))
        messagebox.showinfo("Success", f"Properties exported to:\n{save_path}", parent=window)

def clear_all(entry, textArea):
    entry.config(state="normal")
    entry.delete(0, tk.END)
    entry.config(state="disabled")
    textArea.delete(1.0, tk.END)

