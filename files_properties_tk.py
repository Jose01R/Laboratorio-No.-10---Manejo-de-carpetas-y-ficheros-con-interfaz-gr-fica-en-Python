import os
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from pathlib import Path
from datetime import datetime
from file import File  # Tu clase File

# Variables globales
file_path = None
home_dir = Path.home()
initial_dir = home_dir / "Documents"


def select_file(window, entry, textArea):
    global file_path, initial_dir
    file_path = filedialog.askopenfilename(
        parent=window,
        initialdir=initial_dir,
        title="Select a file",
        filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')]
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
        size = os.path.getsize(file_path)
        created = datetime.fromtimestamp(os.path.getctime(file_path)).strftime("%Y-%m-%d %H:%M:%S")
        modified = datetime.fromtimestamp(os.path.getmtime(file_path)).strftime("%Y-%m-%d %H:%M:%S")
        accessed = datetime.fromtimestamp(os.path.getatime(file_path)).strftime("%Y-%m-%d %H:%M:%S")

        textArea.delete(1.0, tk.END)
        props = (
            f"File: {file_path}\n"
            f"Size: {size} bytes\n"
            f"Created: {created}\n"
            f"Modified: {modified}\n"
            f"Last Accessed: {accessed}\n"
        )
        textArea.insert(tk.INSERT, props)
    except Exception as e:
        messagebox.showerror("Error", f"Cannot get file properties:\n{e}", parent=textArea.master)


def export_properties(window, textArea):
    global file_path, initial_dir
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
        try:
            with open(save_path, "w") as f:
                f.write(textArea.get(1.0, tk.END))
            messagebox.showinfo("Success", f"Properties exported to:\n{save_path}", parent=window)
        except Exception as e:
            messagebox.showerror("Error", f"Cannot export properties:\n{e}", parent=window)


def clear_all(entry, textArea):
    entry.config(state="normal")
    entry.delete(0, tk.END)
    entry.config(state="disabled")
    textArea.delete(1.0, tk.END)
