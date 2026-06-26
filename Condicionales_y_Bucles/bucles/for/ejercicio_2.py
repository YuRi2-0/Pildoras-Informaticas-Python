
lista_1 = ["Juan","pepe",3]
lista_2 = ["Pepe","Juan"]

# def compararListas(lista1,lista2):
#     if len(lista1)!= len(lista2):
#         return False
#     else: 
#         for x in range(0,len(lista1)):
#             if lista1[x] != lista2[x]:
#                 return False
            
#         return True
            
# print(compararListas(lista_1,lista_2))


from collections import Counter

# def compararListas(list1,list2):
#     return Counter(list1) == Counter(list2)

# print(compararListas(lista_1,lista_2))



def comparar_listas(lista1, lista2):
    normalizada1 = [x.strip().casefold() for x in lista1]
    normalizada2 = [x.strip().casefold() for x in lista2]

    return Counter(normalizada1) == Counter(normalizada2)

print(comparar_listas(lista_1,lista_2))