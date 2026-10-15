from tkinter import *

raiz = Tk()

mi_frame = Frame(width="800", height="600")

mi_frame.pack(fill="both", expand="1")
mi_frame.config(bg="#ccc")

# Instanciamos la clase Label
label_1 = Label(mi_frame, text="Hoy es 15 de octubre del 2026", fg="#48e", font="14")
# Con el metodo place establecemos las coordenadas de donde aparacera el widget
label_1.place(x=120, y=125)

raigen_imagen = PhotoImage(file="./imagen/reigen.png")

label_2 = Label(mi_frame, image=raigen_imagen)

label_2.place(x=200, y=180)


# Al usar el metodo pack(), hacemos que nuestro frame se adapte al tamaño del widget
# label_1.pack()


raiz.mainloop()
