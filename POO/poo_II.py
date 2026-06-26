class Persona():
    nombre = ""
    apellido = ""
    edad = 0
    genero = "sin definir"
    
    def __init__(self, nombre, apellido, edad, genero):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.genero = genero
    
    def habla(self):
        return f"La persona llamada {self.nombre} esta hablando"
    
    def caminar(self):
        return f"La persona llamada {self.nombre} esta caminando"
    
    def getDatos(self):
        return f"Nombre : {self.nombre} Apellido : {self.apellido} \nEdad : {self.edad} Genero: {self.genero}"
    
p1 = Persona("Juan","Diaz",21, "masculino")

print(p1.getDatos())