from tkinter import *

raiz = Tk()

raiz.title("Tkinter II")
# raiz.geometry("800x400")
raiz.iconbitmap("./icono/favicon.ico")
raiz.config(bg="#4f2")

# Instanciamos un frame
miFrame = Frame()

# Empaquetamos el frame dentro de la raiz
miFrame.pack(fill="both",expand="1")

miFrame.config(bg="#ccc")

# La raiz se adapta a las dimensiones establecidas por el frame
miFrame.config(width="650",height="350")

raiz.mainloop()