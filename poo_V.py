class Persona:
    
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    
    def getDatosPersonales(self):
        return f" Nombre : {self.nombre}\n Apellido : {self.apellido}\n Edad : {self.edad}\n"
    
    def habla(self):
        return f"Estoy hablando"
    
    def piensa(self):
        return f"Estoy pensando"
    
    def camina(self):
        return f"Estoy caminando"
    
    def come(self):
        return f"Estoy comiendo"
    
    
class Estudiante(Persona):
    
    def __init__(self,nombre,apellido,edad,colegio):
        
        super().__init__(nombre,apellido,edad)
        
        self.colegio = colegio
    
    def getDatosPersonales(self):
        return super().getDatosPersonales() + f" Colegio {self.colegio}"
    
    def estudia(self):
        return 'Estoy estudiando'
    
persona1 = Persona('Ana','Gomez',30)

estudiante1 = Estudiante("Juan","Diaz",20,"Pamer")

print(persona1.getDatosPersonales())
print(estudiante1.getDatosPersonales())