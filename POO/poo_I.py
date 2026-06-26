class Coche():
    ruedas = 4
    largoChasis = 260
    anchoChasis = 130
    arrancado = False
    
    def arrancar(self):
        self.arrancado = True
    
    def estadoCoche(self):
        if(self.arrancado):
            return "El coche esta funcionando"
        else:
            return "El coche esta parado"

mazda = Coche() # ejemplar de clase

print(f"Tu coche está arrancado : {mazda.arrancado}")
mazda.arrancar()
print(f"Tu coche está arrancado : {mazda.arrancado}")
print(mazda.estadoCoche())

