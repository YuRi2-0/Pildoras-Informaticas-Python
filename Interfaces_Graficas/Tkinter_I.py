from tkinter import *

raiz = Tk()

# Metodo que modifica el titulo de la ventana
raiz.title("Primera ventana Tkinter")

# Metodo que redimensiona la ventana
raiz.resizable(1,1) 

# Metodo que establece un nuevo icono para la ventana
raiz.iconbitmap("./icono/favicon.ico")

# Metodo que establece la dimension inicial de la ventana
raiz.geometry("700x400")

# Metodo donde establecemos el background
raiz.config(bg="#ccc")

raiz.mainloop()