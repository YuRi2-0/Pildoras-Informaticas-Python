import random

numero_aleatorio = random.randint(1,10)

intentos = 1
mensaje = ""
while intentos > 0:
    numero_usuario = int(input("Ingrese un numero entre 1 y 10:"))
    if numero_usuario < numero_aleatorio:
        print("El numero aleatorio es mayor que el numero ingresado")
    elif numero_usuario == numero_aleatorio:
        mensaje = f"Correcto! El numero {numero_usuario} es igual que el aleatorio "
        break
    else:
        print("El numero aleatorio es menor que el numero ingresado")
    
    intentos+=1


print(mensaje)
print(f"Intentos consumidos {intentos}")