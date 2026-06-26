class CuentaCorriente():
    numero_cuenta = ''
    titular_cuenta = ''
    saldo_cuenta = 0
    
    def __init__(self,numero_cuenta,titular_cuenta,saldo_cuenta):
        self.numero_cuenta = numero_cuenta
        self.titular_cuenta = titular_cuenta
        self.saldo_cuenta = saldo_cuenta
    
    def getDatos(self):
        return f'n° de cuenta : {self.numero_cuenta}\n Titular de la cuenta : {self.titular_cuenta}\n Saldo : {self.saldo_cuenta}'
    
    def ingresarDinero(self,dinero):
        self.saldo_cuenta += dinero
        print(f'Usted a ingresado : {dinero}')
        
    def retirarDinero(self,dinero):
        self.saldo_cuenta -= dinero
        print(f'Usted a retirado : {dinero}')

    
usuario1 = CuentaCorriente('123456','Jorgue Fernando', 100)

print(usuario1.getDatos())

usuario1.ingresarDinero(100)
usuario1.ingresarDinero(150)

usuario1.retirarDinero(40)

print(usuario1.saldo_cuenta)