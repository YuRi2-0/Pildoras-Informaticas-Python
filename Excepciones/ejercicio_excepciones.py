# • Crea un programa que pida introducir por consola 10 nombres propios de personas.
# • Los nombres se guardarán en una lista.
# • Si introducimos un nombre repetido, el programa lanzará una excepción de tipo
# ValueError, la excepción nos informará del error con el texto “Error. Este nombre ya se
# ha introducido”, y no se guardará el nombre repetido en la lista.
# • Imprimir el contenido de la lista por consola


def guardar_nombres (cant_nombre):
    lista_nombre = []
    for x in range(cant_nombre):
        nombre = input("Ingrese su nombre : ")
        try:
            if nombre in lista_nombre:
                raise ValueError 
            else:
                lista_nombre.append(nombre)
        except:
            print("Error. Este nombre ya se ha introducido")        
            return lista_nombre

cantidad = 4
print(guardar_nombres(cantidad))
