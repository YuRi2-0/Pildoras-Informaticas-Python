from tkinter import *

from tkinter import messagebox as MessageBox

raiz = Tk()

# FRAME
frame = Frame(raiz, width=1000, height=550)
frame.pack(fill="both", expand=1)
frame.config(bg="#ccc")

# nombre = StringVar()

# Text Box
txt_nombre = Entry(frame,font=14)
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

# Texto multilineas
txt_comentarios = Text(frame, width=20, height=10, font=14)
txt_comentarios.grid(row=5, column=1, padx=15, pady=15)

# Barra de desplazamiento vertical (Texto Comentario)
scrollbar_vertical = Scrollbar(frame, command=txt_comentarios.yview)
scrollbar_vertical.grid(row=5, column=2, sticky="nsew")

txt_comentarios.config(yscrollcommand=scrollbar_vertical.set)


# Labels
lbl_nombre = Label(frame, text="Nombre : ", font=14)
lbl_nombre.grid(row=0, column=0, sticky="e")

lbl_apellido = Label(frame, text="Apellido : ", font=14)
lbl_apellido.grid(row=1, column=0, sticky="e")

lbl_contrasena = Label(frame, text="Contraseña : ", font=14)
lbl_contrasena.grid(row=2, column=0, sticky="e")

lbl_correo = Label(frame, text="Correo : ", font=14)
lbl_correo.grid(row=3, column=0, sticky="e")

lbl_direccion_hogar = Label(frame, text="Direccion : ", font=14)
lbl_direccion_hogar.grid(row=4, column=0, sticky="e")

lbl_comentarios = Label(frame, text="Comentarios :", font=14)
lbl_comentarios.grid(row=5, column=0, sticky="e")

def transferir_texto():
    nombre = txt_nombre.get()
    txt_comentarios.insert(END,f"Nombre : {nombre}" + "\n")
    txt_nombre.delete(0,END)
    
botonEnviar = Button(raiz, text="Enviar", command=transferir_texto ,font=14)
botonEnviar.pack()

raiz.mainloop()
