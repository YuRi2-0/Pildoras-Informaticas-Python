num1 = int(input("Ingrese el primer numero:"))
num2 = int(input("Ingrese el segundo numero:"))

def es_primo(numero):
    for n in range(2,numero):
        if numero % n == 0:
            return False
    print(f"{numero} es primo")
    return True

for i in range(num1,num2):
    es_primo(i)