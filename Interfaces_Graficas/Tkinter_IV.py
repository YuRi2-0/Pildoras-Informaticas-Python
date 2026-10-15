from tkinter import *

raiz = Tk()

frame_principal = Frame(raiz, width="800", height="600")
frame_principal.pack(fill="both", expand="1")
frame_principal.config(bg="#ccc")

# Textbox nombre
text_box_nombre = Entry(frame_principal,font=14)
text_box_nombre.grid(row=0, column=1)

# Textbox apellido
text_box_apellido = Entry(frame_principal,font=14)
text_box_apellido.grid(row=1, column=1)

# Textbox edad
text_box_edad = Entry(frame_principal,font=14)
text_box_edad.grid(row=2, column=1)

# Textbox correo
text_box_correo = Entry(frame_principal,font=14)
text_box_correo.grid(row=3, column=1)

# Label nombre
label_nombre = Label(frame_principal, text="Nombre : ", font=14)
label_nombre.grid(row=0, column=0, sticky="w")

# Label apellido
label_apellido = Label(frame_principal, text="Apellido : ", font=14)
label_apellido.grid(row=1, column=0, sticky="w")

# Label edad
label_edad = Label(frame_principal, text="Edad : ", font=14)
label_edad.grid(row=2, column=0, sticky="w")

# Label correo
label_correo = Label(frame_principal, text="Correo : ", font=14)
label_correo.grid(row=3, column=0, sticky="w")


raiz.mainloop()
