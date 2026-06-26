# Crear una clase con el nombre de CuentaCorriente con tres atributos que serán:
# El nº de la cuenta (un string numérico con el nº de cifras que quieras)
# El titular de la cuenta
# El saldo de la cuenta
# Crear un método getter que nos muestre la información de la cuenta. Debe mostrarnos el nº, el titular y el saldo.
# Crear un método que nos permita ingresar dinero en la cuenta
# Crear un método que nos permita retirar dinero de la cuenta

class CuentaCorriente:
    numeroCuenta = ""
    titularCuenta = ""
    saldoCuenta = 0
    
    def __init__(self,numeroCuenta,titularCuenta,saldoCuenta):
        self.numeroCuenta = numeroCuenta
        self.titularCuenta = titularCuenta
        self.saldoCuenta = saldoCuenta
        
    def getDatos(self):
        return f'N° : {self.numeroCuenta}\nTitular : {self.titularCuenta}\nSaldo : {self.saldoCuenta}'
    
    def ingresaDinero(self,dinero):
        dinero += self.saldoCuenta
    
p1 = CuentaCorriente("1234","Jorgue Hernando",100)

print(p1.getDatos())