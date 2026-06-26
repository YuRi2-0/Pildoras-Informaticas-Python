# def generarPares(limite):
    
#     num = 1
    
#     numerosPares = []
    
#     while num < limite:
#         numerosPares.append(num*2)
        
#         num+=1

#     return numerosPares


def generarPares(limite):
    
    num = 1
    
    while num < limite:
        
        yield num * 2
        
        num+=1

sucesionPares = generarPares(4)

# for i in sucesionPares:
#     print(i)

print(next(sucesionPares))
print(next(sucesionPares))
print(next(sucesionPares))
