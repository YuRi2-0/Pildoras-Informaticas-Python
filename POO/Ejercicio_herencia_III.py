class Vehiculo():
    
    def __init__(self, ruedas, color, ancho, alto, marchas):
        self.ruedas = ruedas
        self.color = color
        self.ancho = ancho
        self.alto = alto
        self.marchas = marchas
        
        self.acelerando = False
        self.frenando = False
        self.girando = False
        
    
    def acelerar(self):
        self.acelerando = True
        
    def frenar(self):
        self.frenando = True
    
    def girar(self):
        self.girando = True
        
        
class Coche(Vehiculo):
    def __init__(self, ruedas, color, ancho, alto, marchas, cilindros, asientos, aire_acondicionado):
        super().__init__(ruedas, color, ancho, alto, marchas)
        
        self.cilindros = cilindros
        self.asientos = asientos
        self.aire_acondicionado = aire_acondicionado
        
    def Ir_Marcha_Atras(self):
        
        self.marcha_Atras = True
        
    def Arrancar(self):
        
        self.arrancar = True
        
class Furgoneta(Coche):
    def __init__(self, ruedas, color, ancho, alto, marchas, cilindros, asientos, aire_acondicionado, carga):
        super().__init__(ruedas, color, ancho, alto, marchas, cilindros, asientos, aire_acondicionado)
        
        self.carga = carga
        
    def Cargar(self):
        
        self.cargando = True
        
class Bicicleta(Vehiculo):
    
    def __init__(self, ruedas, color, ancho, alto, marchas):
        super().__init__(ruedas, color, ancho, alto, marchas)
        
    def Saltar(self):
        
        self.saltando = True
    
    def Derrapar(self):
        
        self.derrapando = True
        
class Moto(Coche, Bicicleta):
    def __init__(self, ruedas, color, ancho, alto, marchas, cilindros, asientos, aire_acondicionado):
        super().__init__(ruedas, color, ancho, alto, marchas, cilindros, asientos, aire_acondicionado = False)
        