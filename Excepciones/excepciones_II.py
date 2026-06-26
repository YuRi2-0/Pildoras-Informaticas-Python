def divide():
    try:
        op1= float(input("Introduce el primer numero: "))
        
        op2= float(input("Introduce el primer numero: "))
    
        print(f"El resultado es {str(op1 / op2)}")
    except ZeroDivisionError:
        print("No se puede dividir entre cero")
    except ValueError:
        print("El valor introducido no es numerico")
        
divide()