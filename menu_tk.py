from tkinter import *
from tkinter.font import Font
from tkinter import scrolledtext
import tkinter.ttk as ttk
import file_tk as file

def main_menu():
    main_window = Tk()
    main_window.title("LAB 10")
    main_window.minsize(width=530, height=450)
    main_window.resizable(False, False)

    font_title = Font(family="Arial", size=20)
    font_button = Font(family="Arial", size=14)

    #definimos y mostramos los widgets

    Label(main_window, text="").pack()
    Label(main_window, text="").pack()
    Label(main_window, text="LABORATORY 10 - MAIN MENU", font=font_title).pack()

    #definimos los botones del menu

    button1 = Button(main_window, text="File management", width=30, height=2, font=font_button, bd=3, command=lambda: file_window(main_window))
    button2 = Button(main_window, text="Folder management", width=30, height=2, font=font_button, bd=3, command=lambda: folder_window(main_window))
    button3 = Button(main_window, text="Searching files management", width=30, height=2, font=font_button, bd=3, command=lambda: search_window(main_window))
    button4 = Button(main_window, text="Files properties", width=30, height=2, font=font_button, bd=3, command=lambda: property_window(main_window))
    button5 = Button(main_window, text="Exit", width=30, height=2, font=font_button, bd=3, command= exit)

    #mostrar por pantalla los widget
    button1.pack()
    button2.pack()
    button3.pack()
    button4.pack()
    button5.pack()

    #procedemos a iniciar la intefaz

    main_window.mainloop()

def file_window(parent_window):
    window = Toplevel(parent_window)  
    window.title("FILES MANAGEMENT")
    window.minsize(width=310, height=530)
    window.resizable(False, False)

    font_title = Font(family="Arial", size=20)
    font_button = Font(family="Arial", size=14)

    #definimos y mostramos los widgets

    Label(window, text="").pack()
    Label(window, text="").pack()
    Label(window, text="FILES MANAGEMENT", font=font_title).pack()

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

    font_widget = Font(family="Arial", size=20)

    #crear widget Scrolledtext para mostrar el conenido del archivo
    textArea = scrolledtext.ScrolledText(window, wrap="word", width=70, height=10, font=Font(family="Arial", size=20))
    textArea.pack(padx=10, pady=10)

    #definimos array de btn
    buttons = []

    #definimos los botones del menu

    openBtn = Button(window, text="Open file", width=10, height=1, font=font_button, bd=3, command=lambda: file.open_file(window, file_name, textArea, buttons))
    returnBtn = Button(window, text="CLose", width=10, height=1, font=font_button, bd=3, command= window.destroy)

    

    #mostrar por pantalla los widget
    openBtn.pack(side = LEFT)
    returnBtn.pack(side = LEFT)
    
    #procedemos a iniciar la intefaz

    window.mainloop() 


