import sys

def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplica(num1, num2):
    return num1 * num2

def divide(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
        return "Operacion fallida"

intentos = 0
while True:
    try:
        op1 = int(input("Ingrese el primer numero: "))

        op2 = int(input("Ingrese el segundo numero: "))
        
        break
    except ValueError:
        intentos+=1
        print("El valor introducido no es correcto")
        if intentos == 3:
            sys.exit()

operacion = input("Introduce la operacion a realizar (suma, resta, multiplica, divide):")

if operacion == "suma":
    print(suma(op1,op2))
    
elif operacion == "resta":
    print(resta(op1,op2))
    
elif operacion == "multiplica":
    print(multiplica(op1,op2))

elif operacion == "divide":
    print(divide(op1,op2))
    
else:
    print("Operacion no contemplada")