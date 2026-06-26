class Persona:
    __nombre = ""
    apellido = ""
    __edad = 0
    genero = "sin definir"
    
    def __init__(self, nombre, apellido, genero):
        self.__nombre = nombre
        self.apellido = apellido
        self.genero = genero
        
    def setEdad(self,edad):
        
        if edad < 0 or edad > 100:
            return 'Error en la edad'
        else:
            self.__edad = edad    
            return self.__edad
    
    def habla(self):
        return f'La persona llamada {self.__nombre} esta hablando'
    
    def camina(self):
        return f'La persona llamada {self.__nombre} esta caminando'
    
    def getDatos(self):
        return f' Nombre : {self.__nombre}\n Apellido : {self.apellido}\n Edad : {self.__edad}\n Genero : {self.genero}'
    
p1 = Persona('Juan',"Diaz", "masculino")

p1.setEdad(52)

print(p1.getDatos())

