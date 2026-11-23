"""Crear una clase calculadora, con las siguientes características:
a. Dos atrubutos donde se guardarán los números con los que se va a operar.
b. Tendrá los siguientes métodos:
    sumar() Devuelve la suma
    restar() Devuelve la resta
    multiplicar() Devuelve la multiplicación
    dividir() Devuelve la división del mayor entre el menor
"""

class CALCULADORA:
#    a,b=0,0
    def __init__(self,a,b):    # Esto es un constructor
        self.a = a
        self.b = b
    def sumar(self):
        return self.a + self.b
    def restar(self):
        return self.a-self.b
    def multiplicar(self):
        return max(self.a,self.b)*min(self.a,self.b)
    def dividir(self):
        return max(self.a,self.b)/min(self.a,self.b)