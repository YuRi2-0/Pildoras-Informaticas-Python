# i = 0
# j = 0
# while i < 3:
#     while j < 3:
#         print(i,j)
#         j += 1
#     i += 1
#     j = 0

# a, b = 0, 1
# while b < 25:
#     print(b)
#     a, b = b, a + b

a = 0
b = 1
lista = []


for x in range(8 ):
    lista.append(str(a))
    a,b = b, a+b
    
print(' '.join(lista))