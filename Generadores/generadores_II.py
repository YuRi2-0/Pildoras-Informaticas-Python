def capitales_mundo(*ciudades):
    for capital in ciudades:
        yield from capital
            
        
        
capitales_devueltas = capitales_mundo('Berlin', 'Roma', 'Bogota', 'Pekin', 'Hanoi')

print(next(capitales_devueltas))
print(next(capitales_devueltas))
print(next(capitales_devueltas))
print(next(capitales_devueltas))
print(next(capitales_devueltas))