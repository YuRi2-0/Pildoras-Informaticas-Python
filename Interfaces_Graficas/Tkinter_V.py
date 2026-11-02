from tkinter import *

raiz = Tk()

# FRAME
frame = Frame(raiz, width=1000, height=550)
frame.pack(fill="both", expand=1)
frame.config(bg="#ccc")

# Text Box
txt_nombre = Entry(frame, font=14)
txt_nombre.grid(row=0, column=1, padx=15, pady=15)

txt_apellido = Entry(frame, font=14)
txt_apellido.grid(row=1, column=1, padx=15, pady=15)

txt_contrasena = Entry(frame, font=14)
txt_contrasena.grid(row=2, column=1, padx=15, pady=15)
txt_contrasena.config(show="*")

txt_correo = Entry(frame, font=14)
txt_correo.grid(row=3, column=1, padx=15, pady=15)

txt_direccion_hogar = Entry(frame, font=14)
txt_direccion_hogar.grid(row=4, column=1, padx=15, pady=15)

texto_comentarios = Text(frame, width=20, height=10, font=14)
texto_comentarios.grid(row=5, column=1, padx=15, pady=15)


# Labels
label_nombre = Label(frame, text="Nombre : ", font=14)
label_nombre.grid(row=0, column=0, sticky="e")

label_apellido = Label(frame, text="Apellido : ", font=14)
label_apellido.grid(row=1, column=0, sticky="e")

label_contrasena = Label(frame, text="Contraseña : ", font=14)
label_contrasena.grid(row=2, column=0, sticky="e")

label_correo = Label(frame, text="Correo : ", font=14)
label_correo.grid(row=3, column=0, sticky="e")

label_direccion_hogar = Label(frame, text="Direccion : ", font=14)
label_direccion_hogar.grid(row=4, column=0, sticky="e")

label_comentarios = Label(frame, text="Comentarios :", font=14)
label_comentarios.grid(row=5, column=0, sticky="e")

botonEnviar = Button(raiz, text="Enviar",font=14)
botonEnviar.pack()

raiz.mainloop()
