from tkinter import *

raiz = Tk()

frame = Frame(raiz)

frame.pack()

operacion = ""
resultado = 0

digito_display = StringVar()

display = Entry(frame, font="Arial 30", textvariable=digito_display)

display.grid(row=1, column=1, columnspan=4, pady=10)
display.config(background="#000", fg="#00db00", justify="right")

# ------------------------- pulsaciones numeros -------------------------


def pulsacionesTeclas(numPulsado):

    global operacion
    
    if operacion != "":
        digito_display.set(numPulsado)
        operacion = ""
    else:
        digito_display.set(digito_display.get() + numPulsado)

# ------------------------- funcion suma -------------------------

def suma(num):
    
    global operacion
    
    global resultado
    
    resultado+=int(num)
    
    operacion = "suma"
    
    digito_display.set(resultado)

    
# ------------------------- funcion total -------------------------

def total():
    global resultado
    
    digito_display.set(resultado + int(digito_display.get()))
    resultado = 0



# ------------------------- PRIMERA FILA -------------------------



boton7 = Button(frame, text="7", width=15, command=lambda: pulsacionesTeclas("7"))
boton7.grid(row=2, column=1)

boton8 = Button(frame, text="8", width=15, command=lambda: pulsacionesTeclas("8"))
boton8.grid(row=2, column=2)

boton9 = Button(frame, text="9", width=15, command=lambda: pulsacionesTeclas("9"))
boton9.grid(row=2, column=3)

btn_dividir = Button(frame, text="/", width=15)
btn_dividir.grid(row=2, column=4)

# ------------------------- SEGUNDA FILA -------------------------
boton4 = Button(frame, text="4", width=15, command=lambda: pulsacionesTeclas("4"))
boton4.grid(row=3, column=1)

boton5 = Button(frame, text="5", width=15, command=lambda: pulsacionesTeclas("5"))
boton5.grid(row=3, column=2)

boton6 = Button(frame, text="6", width=15, command=lambda: pulsacionesTeclas("6"))
boton6.grid(row=3, column=3)

btn_multiplicar = Button(frame, text="x", width=15)
btn_multiplicar.grid(row=3, column=4)

# ------------------------- TERCERA FILA -------------------------
boton1 = Button(frame, text="1", width=15, command=lambda: pulsacionesTeclas("1"))
boton1.grid(row=4, column=1)

boton2 = Button(frame, text="2", width=15, command=lambda: pulsacionesTeclas("2"))
boton2.grid(row=4, column=2)

boton3 = Button(frame, text="3", width=15, command=lambda: pulsacionesTeclas("3"))
boton3.grid(row=4, column=3)

btn_restar = Button(frame, text="-", width=15)
btn_restar.grid(row=4, column=4)

# ------------------------- CUARTO FILA -------------------------
boton0 = Button(frame, text="0", width=15, command=lambda: pulsacionesTeclas("0"))
boton0.grid(row=5, column=1)

boton_coma = Button(frame, text=",", width=15, command=lambda: pulsacionesTeclas("."))
boton_coma.grid(row=5, column=2)

btn_igual = Button(frame, text="=", width=15, command=lambda:total())
btn_igual.grid(row=5, column=3)

btn_sumar = Button(frame, text="+", width=15, command=lambda:suma(digito_display.get()))
btn_sumar.grid(row=5, column=4)


raiz.mainloop()
