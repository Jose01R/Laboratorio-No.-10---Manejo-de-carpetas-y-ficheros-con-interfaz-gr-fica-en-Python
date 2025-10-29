from tkinter import *
from tkinter.font import Font
from tkinter import scrolledtext
import tkinter.ttk as ttk
import file_tk as file
import tkinter as tk
import files_properties_tk as fp
def main_menu():
    main_window = Tk()
    main_window.title("LAB 10")
    main_window.minsize(width=530, height=450)
    main_window.resizable(False, False)

    font_title = Font(family="Arial", size=20)
    font_button = Font(family="Arial", size=14)

    Label(main_window, text="").pack()
    Label(main_window, text="").pack()
    Label(main_window, text="LABORATORY 10 - MAIN MENU", font=font_title).pack()

    # Botones del menú principal
    button1 = Button(main_window, text="File management", width=30, height=2, font=font_button, bd=3,
                     command=lambda: file_window(main_window))
    button2 = Button(main_window, text="Folder management", width=30, height=2, font=font_button, bd=3)
    button3 = Button(main_window, text="Searching files management", width=30, height=2, font=font_button, bd=3)
    button4 = Button(main_window, text="Files properties", width=30, height=2,
           font=font_button, bd=3,
           command=lambda: files_properties_window(main_window))
    button5 = Button(main_window, text="Exit", width=30, height=2, font=font_button, bd=3, command=exit)

    button1.pack()
    button2.pack()
    button3.pack()
    button4.pack()
    button5.pack()

    main_window.mainloop()


def file_window(parent_window):
    window = Toplevel(parent_window)
    window.title("FILES MANAGEMENT")
    window.minsize(width=650, height=600)
    window.resizable(False, False)

    font_title = Font(family="Arial", size=20)
    font_button = Font(family="Arial", size=14)

    Label(window, text="").pack()
    Label(window, text="FILES MANAGEMENT", font=font_title).pack()

    # Frame para ruta
    frame = Frame(window)
    frame.pack(padx=10, pady=10)

    Label(frame, text="Path/name: ").pack(side=LEFT, padx=5)

    file_name = Entry(frame, width=50, font=Font(family="Arial", size=14))
    file_name.config(state="disabled")
    file_name.pack(side=LEFT, padx=5)

    # Área de texto
    textArea = scrolledtext.ScrolledText(window, wrap="word", width=70, height=15, font=Font(family="Arial", size=14))
    textArea.pack(padx=10, pady=10)

    # Botones
    buttons_frame = Frame(window)
    buttons_frame.pack(pady=10)

    Button(buttons_frame, text="Open File", width=10, font=font_button, bd=3,
       command=lambda: file.open_file(window, file_name, textArea)).grid(row=0, column=0, padx=5, pady=5)

    Button(buttons_frame, text="Save", width=10, font=font_button, bd=3,
        command=lambda: file.save_file(window, file_name, textArea)).grid(row=0, column=1, padx=5, pady=5)

    Button(buttons_frame, text="Save As", width=10, font=font_button, bd=3,
        command=lambda: file.save_as_file(window, file_name, textArea)).grid(row=0, column=2, padx=5, pady=5)

    Button(buttons_frame, text="Delete", width=10, font=font_button, bd=3,
        command=lambda: file.delete_file(window, file_name, textArea)).grid(row=1, column=0, padx=5, pady=5)

    Button(buttons_frame, text="Clear", width=10, font=font_button, bd=3,
        command=lambda: file.clear_text(file_name, textArea)).grid(row=1, column=1, padx=5, pady=5)

    Button(buttons_frame, text="Close", width=10, font=font_button, bd=3,
        command=window.destroy).grid(row=1, column=2, padx=5, pady=5)


    window.mainloop()

def files_properties_window(parent_window):
    window = tk.Toplevel(parent_window)
    window.title("FILES PROPERTIES")
    window.minsize(width=650, height=500)
    window.resizable(False, False)

    font_title = tk.font.Font(family="Arial", size=20)
    font_button = tk.font.Font(family="Arial", size=14)

    tk.Label(window, text="").pack()
    tk.Label(window, text="FILES PROPERTIES", font=font_title).pack()

    # Frame para ruta
    frame = tk.Frame(window)
    frame.pack(padx=10, pady=10)
    tk.Label(frame, text="Path/name: ").pack(side=tk.LEFT, padx=5)

    file_name_entry = tk.Entry(frame, width=50, font=tk.font.Font(family="Arial", size=14))
    file_name_entry.config(state="disabled")
    file_name_entry.pack(side=tk.LEFT, padx=5)

    # Área de texto
    textArea = scrolledtext.ScrolledText(window, wrap="word", width=70, height=15,
                                         font=tk.font.Font(family="Arial", size=14))
    textArea.pack(padx=10, pady=10)

    # Botones
    buttons_frame = tk.Frame(window)
    buttons_frame.pack(pady=10)

    tk.Button(buttons_frame, text="Select File", width=15, font=font_button, bd=3,
              command=lambda: fp.select_file(window, file_name_entry, textArea)).grid(row=0, column=0, padx=5, pady=5)
    tk.Button(buttons_frame, text="Export Properties", width=15, font=font_button, bd=3,
              command=lambda: fp.export_properties(window, textArea)).grid(row=0, column=1, padx=5, pady=5)
    tk.Button(buttons_frame, text="Clear", width=15, font=font_button, bd=3,
              command=lambda: fp.clear_all(file_name_entry, textArea)).grid(row=1, column=0, padx=5, pady=5)
    tk.Button(buttons_frame, text="Close", width=15, font=font_button, bd=3,
              command=window.destroy).grid(row=1, column=1, padx=5, pady=5)

if __name__ == "__main__":
    main_menu()



