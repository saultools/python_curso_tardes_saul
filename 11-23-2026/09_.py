class Cuenta:
    def __init__(self,saldo):
        self.saldo=saldo
    def ingresar(self,cantidad):
        self.saldo+=cantidad
    def extraer(self,cantidad):
        self.saldo-=cantidad

# Crear la clase CuentaLimitada, que será una subclase de Cuenta, y tendrá un atributo con la cantidad máxima a extraer.
# Si el valor del atributo es 0, no hay límite. Si es >0, ese será el límite, y no se podrá extraer más dinero que el que marque el límite.

class CuentaLimitada(Cuenta):
    def __init__(self, saldo, limitada):
        super().__init__(saldo)
        self.limitada=limitada
    def extraer(self, cantidad):
        if self.limitada >= 0 and cantidad > self.limitada:
            super().extraer(self.limitada)
        else: 
            super().extraer(cantidad)

cl=CuentaLimitada(200,50)
cl.extraer(20)
print(cl.saldo)
cl.extraer(100)
print(cl.saldo)

# Crear una nueva clase que herede CuentaLimitada, llamada CuentaMovimientos. 
# Cada vez que se ingrese o extraiga, se deberá registrar dicho moimiento.
# Un movimiento tiene dos propiedades: cantidad y tipo (ingreso o extracción).
# La nueva clase tendrá un método que devuelve la lista de los últimos cinco movimientos.

class CuentaMovimientos(CuentaLimitada):
    def __init__(self, saldo, limitada):
        super().__init__(saldo, limitada)
        self.movimientos = []
    def ingresar(self, cantidad):
        super().ingresar(cantidad)
        self.movimientos.append({"tipo": "ingreso", "cantidad": cantidad})
    def extraer(self, cantidad):
        super().extraer(cantidad)
        self.movimientos.append({"tipo": "extracción", "cantidad": cantidad})
    def get_ultimos_movimientos(self, n=5):
        return self.movimientos[-n:]

cl = CuentaMovimientos(200, 50)
cl.ingresar(30)
cl.extraer(20)
cl.extraer(100)
print(cl.get_ultimos_movimientos())
print(f"saldo: {cl.saldo}")