class CuentaCorriente():
    numero_cuenta = ''
    titular_cuenta = ''
    saldo_cuenta = 0
    
    def __init__(self,numero_cuenta,titular_cuenta,saldo_cuenta):
        self.numero_cuenta = numero_cuenta
        self.titular_cuenta = titular_cuenta
        self.saldo_cuenta = saldo_cuenta
    
    def getDatos(self):
        return f' n° de cuenta : {self.numero_cuenta}\n Titular de la cuenta : {self.titular_cuenta}\n Saldo : {self.saldo_cuenta}\n'
    
    def ingresarDinero(self,dinero):
        self.saldo_cuenta += dinero
        print(f'Usted a ingresado : {dinero}')
        
    def retirarDinero(self,dinero):
        self.saldo_cuenta -= dinero
        print(f'Usted a retirado : {dinero}')


class CuentaJoven(CuentaCorriente):
    
    def __init__(self,numero_cuenta,titular_cuenta,saldo_cuenta,bonus_promocion = 0):
        super().__init__(numero_cuenta,titular_cuenta,saldo_cuenta)
        
        self.bonus_promocion = bonus_promocion
        self.saldo_cuenta += bonus_promocion        
    
    def getDatos(self):
        return super().getDatos() + f" Bonus: {self.bonus_promocion}"
    
    def getBonus(self):
        return f"Bono : {self.bonus_promocion}"
    
p1 = CuentaJoven("1234","Ana",100,100)

p1.ingresarDinero(20)
p1.retirarDinero(45)



print(p1.getDatos())