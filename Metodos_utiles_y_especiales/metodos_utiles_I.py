class Persona():
    
    almacen_datos = []
    
    # *args    == numero indefinido de parametros almacenados en una tupla
    # **kwargs == '                                         ' en un diccionario
    
    
    def __init__(self, *datos):
        
        for dato in datos:
            
            self.almacen_datos.append(dato)
        
        self.getDatos(self.almacen_datos)

    
    def getDatos(self, info):
        
        for dato in  info:
            print(dato)

p1 = Persona("Juan","Diaz",18)

print(p1)