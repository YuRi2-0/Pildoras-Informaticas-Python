# contador = 0
# while contador < 10:
#     print("holi")
#     contador+=1
# else:
#     print("Bucle finalizado")

# intentos = 0
# while intentos < 3:
#     edad = int(input("Ingrese su edad : "))
#     mensaje = "" 
#     if edad < 18:
#         mensaje = "Acceso denegado"
#         print("Edad no permitida")
#         intentos+=1
#     else:
#         mensaje = "Acceso permitido"
#         break

# print(mensaje)

edad = int(input("Ingrese su edad :"))

while edad < 18 or edad > 100:
    print("Edad no valida")
    edad = int(input("Ingrese su edad :"))
print("Bucle finalizado")