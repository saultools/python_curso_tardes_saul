class COLOR:
    r,g,b=0,0,0
    def colorear(self):
        self.r,self.g,self.b=100,120,200
class RECTANGULO:
    alto=0
    ancho=0
    col=COLOR()
    def area(self):
        return self.alto*self.ancho
    def perimetro(self):
        return self.alto*2+self.ancho*2
    def aumentar(self,valor):
        self.alto+=valor
        self.ancho+=valor
    def dibujar(self):
        for b in range(0,self.ancho):
            print("*",end="")
        for a in range(0,self.alto):
            print("*"+" "*(self.ancho-2)+"*")
        for b in range(0,self.ancho):
            print("*",end="")
        print()

r1 = RECTANGULO()
r2 = RECTANGULO()

r1.alto=5
r1.ancho=10

r2.alto=6
r2.ancho=3

r1.col.colorear()
r2.col.colorear()

r1.dibujar()

print(f"area del 1er rectangulo {r1.area()}")
print(f"perimetro del 2º rectangulo {r2.perimetro()}")
