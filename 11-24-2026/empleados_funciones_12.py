# ver enunciado en el pdf 12
class Empleado():
    def __init__(self,nombre,edad,salario_base):
        self.nombre=nombre
        self.edad=edad
        self.salario_base=salario_base
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
    def calcular_salario(self):
        print(f"Salario base: {self.salario_base}")

class Desarrollador(Empleado):
    def __init__(self, nombre, edad, salario_base,lenguaje,horas_extra):
        super().__init__(nombre, edad, salario_base)
        self.lenguaje=lenguaje
        self.horas_extra=horas_extra
    def calcular_salario(self):
        print(f"Salario a fecha: {Empleado(self.salario_base)+self.horas_extra*25}")
    def mostrar_informacion(self):
            print(f"Nombre: {self.nombre}")
            print(f"Edad: {self.edad}")
            print(f"Lenguaje: {self.lenguaje}")
            print(f"Horas extra a fecha: {self.horas_extra}")

class Gerente(Empleado):
    def __init__(self, nombre, edad, salario_base,departamento,bonus):
          super().__init__(nombre, edad, salario_base)
          self.departamento=departamento
          self.bonus=bonus
    def calcular_salario(self):
        print(f"Salario a fecha: {self.salario_base+self.bonus}")
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Bono estipulado: {self.bono}")
        print(f"Departamento: {self.departamento}")

empleados = [
    Desarrollador("Carlos", 30, 2500, "Python", 10), 
    Desarrollador("Ana", 28, 2400, "Java", 5), 
    Gerente("Laura", 35, 2800, "Tecnología", 500), 
    Gerente("Pedro", 45, 3000, "Ventas", 700)
    ]