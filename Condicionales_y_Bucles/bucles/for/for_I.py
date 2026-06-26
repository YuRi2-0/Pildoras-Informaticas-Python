a = [1,2,3,4,5]
b = [1,2,3,4,5]



def compararListas(lista1,lista2):
    if (len(lista1)!=len(lista2)) :
        return False
    else:
        
        for x in range(0,len(lista1)):
            if lista1[x] != lista2[x]:
                return False
        
        return True

print(compararListas(a,b))