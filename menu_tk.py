from tkinter import *
from tkinter.font import Font
from tkinter import scrolledtext
import tkinter.ttk as ttk
import file_tk as file
import tkinter as tk
import files_properties_tk as fp
import folder_tk as folder
import searching_files_tk as sf

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
    button3 = Button(main_window, text="Searching files management", width=30, height=2, font=font_button, bd=3, command=lambda: searching_files_window(main_window))
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


def folder_window(parent_window):
    window = Toplevel(parent_window)  
    window.title("FOLDERS MANAGEMENT")
    window.minsize(width=310, height=530)
    window.resizable(False, False)

    font_title = Font(family="Arial", size=20)
    font_button = Font(family="Arial", size=14)

    #definimos y mostramos los widgets
    Label(window, text="").pack()
    Label(window, text="").pack()
    Label(window, text="FOLDERS MANAGEMENT", font=font_title).pack()

    #creamos un frame para contener el siguiente label y entry
    frame = Frame(window)
    frame.pack(padx=10, pady=10)

    #def y colocar un label
    label = Label(frame, text="Path/name: ")
    label.pack(side=LEFT, padx=5)

    #CREAMOS UN ENTRY
    file_name = Entry(frame, width=60, font=Font(family="Arial", size=20))
    file_name.config(state="disabled")
    file_name.pack(side=LEFT, padx=5)

    #crear widget Scrolledtext para mostrar el conenido del archivo
    textArea = scrolledtext.ScrolledText(window, wrap="word", width=70, height=10, font=Font(family="Arial", size=20))
    textArea.pack(padx=10, pady=10)

   
    # Inicializar lista de botones a controlar
    buttons = []
    initial_state = "disabled"

    #Definir los botones
    openBtn = Button(window, text="Open folder", width=10, height=1, font=font_button, bd=3, command=lambda: folder.open_folder(window, file_name, textArea, buttons))
    browseBtn = Button(window, text="Browse folder", width=10, height=1, font=font_button, bd=3, command=lambda: folder.browse_folder(window, file_name, textArea, buttons))
    
    #botones que deben ser controlados (Inicialmente deshabilitados)
    saveAsBtn = Button(window, text="Save folder as", width=10, height=1, font=font_button, bd=3, state=initial_state, command=lambda: folder.save_folder_as(window, file_name, textArea, buttons))
    deleteBtn = Button(window, text="Delete folder", width=10, height=1, font=font_button, bd=3, state=initial_state, command=lambda: folder.delete_folder(window, file_name, textArea, buttons))
    
    clearBtn = Button(window, text="Clear", width=10, height=1, font=font_button, bd=3, command=lambda: folder.clear(window, file_name, textArea, buttons))
    returnBtn = Button(window, text="CLose", width=10, height=1, font=font_button, bd=3, command= window.destroy)

    #Rellenar  lista de botones después de definirlos
    buttons.append(saveAsBtn) # buttons[0]
    buttons.append(deleteBtn) # buttons[1]
    
    # -----------------------------------------------------------

    #mostrar por pantalla los widget
    openBtn.pack(side = LEFT)
    browseBtn.pack(side = LEFT)
    saveAsBtn.pack(side = LEFT)
    deleteBtn.pack(side = LEFT)
    clearBtn.pack(side = LEFT)
    returnBtn.pack(side = LEFT)
    
    #procedemos a iniciar la intefaz
    window.mainloop()

def searching_files_window(parent_window):
    window = tk.Toplevel(parent_window)
    window.title("SEARCHING FILES")
    window.minsize(width=650, height=550)
    window.resizable(False, False)

    font_title = Font(family="Arial", size=20)
    font_label = Font(family="Arial", size=14)
    font_entry = Font(family="Arial", size=14)
    font_button = Font(family="Arial", size=14)
    
    tk.Label(window, text="").pack()
    tk.Label(window, text="SEARCHING FILES", font=font_title).pack(pady=5)

    # --- Carpeta Base (Base Folder Path) ---
    frame_base_path = tk.Frame(window)
    frame_base_path.pack(fill='x', padx=10, pady=5)
    
    tk.Label(frame_base_path, text="Base Folder Path:", font=font_label).pack(side=tk.LEFT, padx=(0, 5))
    
    folder_path = tk.Entry(frame_base_path, width=45, font=font_entry)
    folder_path.config(state="readonly") #inicia como solo lectura
    folder_path.pack(side=tk.LEFT, expand=True, fill='x')

    # --- Patron de busq (Searching Pattern) ---
    frame_pattern = tk.Frame(window)
    frame_pattern.pack(fill='x', padx=10, pady=5)
    
    tk.Label(frame_pattern, text="Searching pattern (*.txt, *.py, report.pdf):", font=font_label).pack(side=tk.LEFT, padx=(0, 5))
    
    pattern_entry = tk.Entry(frame_pattern, width=25, font=font_entry)
    pattern_entry.pack(side=tk.LEFT, expand=False)
    
    # --- TXT AREA (ScrolledText) ---
    frame_results = tk.Frame(window, borderwidth=1, relief="sunken") 
    frame_results.pack(padx=10, pady=10, fill='both', expand=True)

    results_box = scrolledtext.ScrolledText(frame_results, wrap="word", width=60, height=12, 
                                               font=font_label, relief='flat', state=tk.DISABLED) #Iinicialmente  solo lectura
    results_box.pack(padx=2, pady=2, fill='both', expand=True)
    
    # --- Botones  ---
    button_frame = tk.Frame(window)
    button_frame.pack(pady=10)
    
    tk.Button(button_frame, text="Select Folder", width=12, height=1, font=font_button, bd=3,
              command=lambda: sf.select_folder(window, folder_path)).grid(row=0, column=0, padx=5)
              
    tk.Button(button_frame, text="Search File", width=12, height=1, font=font_button, bd=3,
              command=lambda: sf.search_files(window, folder_path, pattern_entry, results_box)).grid(row=0, column=1, padx=5)
              
    tk.Button(button_frame, text="Clear", width=12, height=1, font=font_button, bd=3,
              command=lambda: sf.clear_text(folder_path, pattern_entry, results_box)).grid(row=0, column=2, padx=5)
              
    tk.Button(button_frame, text="Close", width=12, height=1, font=font_button, bd=3,
              command=window.destroy).grid(row=0, column=3, padx=5)

    window.mainloop()