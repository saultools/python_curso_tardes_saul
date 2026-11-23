"""demostración incial
class Lista_Numerica(list): 
    pass

ln=Lista_Numerica()
ln.append("hello")
print(ln)"""

#Crear una subclase de list para el almacenamiento de números con las siguientes características:
# incluirá los métodos:
#    sum(). Devueleve la suma de los números almacenados
#    mean() Devueleve la media de los números almacenados
#Además de estos métodos, el constructor recibirá un parámetro booleano que, en caso de ser true; impedirá que re repitan números

class Lista_Numerica(list):
    def __init__(self, unique):
        self.unique=unique
    def sum(self):
        return sum(self)
    def mean(self):
        if len(self)==0:
            return 0
        return sum(self)/len(self)
    def append(self, object):
        if self.unique and object in self:
            return None
        return super().append(object)

lst=Lista_Numerica(True)
lst.append(5)
lst.append(10)
lst.append(5)
print(f"suma total: {lst.sum()}")
print(f"Media: {lst.mean()}")
