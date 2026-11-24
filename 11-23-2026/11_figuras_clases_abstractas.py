import abc,math 

class Figura(abc.ABC):
    def __init__(self,color):
        self.color=color
    @abc.abstractmethod
    def superficie(self):
        pass

class Circulo(Figura):
    def __init__(self, color,radio):
        super().__init__(color)
        self.radio=radio
    def superficie(self):
        return math.pi*self.radio*self.radio
        
class Triangulo(Figura):
    def __init__ (self, color,base,altura):
        super().__init__(color)
        self.base=base
        self.altura=altura
    def superficie(self):
        return self.base*self.altura/2

def mostrar_datos(fig):
    print(f"color de la figura: {fig.color}")
    print(f"superfie de la figura: {fig.superficie}")
    if isinstance(fig,Circulo):
        print(f"Radio: {fig.radio}")
    if isinstance(fig,Triangulo):
        print(f"base: {fig.base}, altura: {fig.altura}")

mostrar_datos(Circulo("naranja",5))
mostrar_datos(Triangulo("azul",10,5))