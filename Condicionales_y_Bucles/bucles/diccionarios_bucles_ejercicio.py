paises={
}

pais= input("Introduce el pais:")
while pais != "salir":
    ciudad= input("Introduce ciudad:")
    
    lista_ciudades = paises.setdefault(pais,[])
    
    if ciudad not in lista_ciudades:
        lista_ciudades.append(ciudad)
    else:
        print("No puedes volver a agregar la mismaa ciudad a este pais")
        
    pais = input("Introduce el pais")
    
print(paises)
    
