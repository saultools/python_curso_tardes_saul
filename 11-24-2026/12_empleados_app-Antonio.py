# ver enunciado en el pdf 12
class Empleado: 
    def __init__(self, nombre, edad, salario_base): 
        self.nombre = nombre 
        self.edad = edad 
        self.salario_base = salario_base 
    def mostrar_informacion(self): 
            print(f"Nombre: {self.nombre}") 
            print(f"Edad: {self.edad}") 
            print(f"Salario base: {self.salario_base} €") 
 
    def calcular_salario(self): 
        return self.salario_base
class Desarrollador(Empleado): 
 
    def __init__(self, nombre, edad, salario_base, 
                 lenguaje, horas_extra): 
 
        super().__init__(nombre, edad, salario_base) 
 
        self.lenguaje = lenguaje 
        self.horas_extra = horas_extra 
 
    def mostrar_informacion(self): 
        super().mostrar_informacion() 
        print(f"Lenguaje: {self.lenguaje}") 
        print(f"Horas extra: {self.horas_extra}") 
 
    def calcular_salario(self): 
        return super().calcular_salario() + self.horas_extra * 25
class Gerente(Empleado): 
 
    def __init__(self, nombre, edad, salario_base, 
                 departamento, bonus): 
 
        super().__init__(nombre, edad, salario_base) 
 
        self.departamento = departamento 
        self.bonus = bonus 
 
    def mostrar_informacion(self): 
        super().mostrar_informacion() 
        print(f"Departamento: {self.departamento}") 
        print(f"Bonus: {self.bonus} €") 
 
    def calcular_salario(self): 
        return super().calcular_salario() + self.bonus 

    
#programa principal
empleados = [ 
    Desarrollador("Carlos", 30, 2500, "Python", 10), 
    Desarrollador("Ana", 28, 2400, "Java", 5), 
    Gerente("Laura", 35, 2800, "Tecnología", 500), 
    Gerente("Pedro", 45, 3000, "Ventas", 700)
] 

importe_nominas=0
for emp in empleados:
    print("******Información de empleado********")
    emp.mostrar_informacion()
    importe_nominas+=emp.calcular_salario()
print(f"Importe total de nóminas: {importe_nominas}") 
