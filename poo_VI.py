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
        
        Persona.__init__(self,nombre,apellido,edad)
        
        self.colegio = colegio
    
    def getDatosPersonales(self):
        return super().getDatosPersonales() + f" Colegio {self.colegio}\n"
    
    def estudia(self):
        return 'Estoy estudiando'


class Trabajador(Persona):
    
    def __init__(self, nombre, apellido, edad,empresa):
        Persona.__init__(self,nombre, apellido, edad)
        
        self.empresa = empresa

    def getDatosPersonales(self):
        return super().getDatosPersonales() + f" Empresa : {self.empresa}'\n"

    def trabaja(self):
        return 'Estoy trabajando'


class Director(Trabajador, Estudiante):
    
    def __init__(self,nombre,apellido,edad,empresa,colegio,bonus):
        
        Trabajador.__init__(self,nombre,apellido,edad,empresa)
        
        Estudiante.__init__(self,nombre,apellido,edad,colegio)
        
        self.bonus = bonus

    def getDatosPersonales(self):
        return super().getDatosPersonales() + f" Bonus : {self.bonus}"
    
    def dirige(self):
        return 'Estoy dirigiendo'




persona1 = Persona('Ana','Gomez',30)

estudiante1 = Estudiante("Juan","Diaz",20,"Pamer")


print(persona1.getDatosPersonales())
print(estudiante1.getDatosPersonales())
print("----------------------------------------------------")

director1 = Director('Manuel','Gonzales',42,"Popeyes","UNAC",1400)

print(director1.getDatosPersonales())