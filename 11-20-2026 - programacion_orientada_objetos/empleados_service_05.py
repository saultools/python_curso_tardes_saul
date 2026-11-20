import csv

class Empleado:
    def __init__(self,nombre,edad,salario,departamento):
        self.nombre=nombre
        self.edad=edad
        self.salario=salario
        self.departamento=departamento

class Gestor_Empleados:
    def __init__(self,dir):
        self.dir=dir
    
    def alta_empleado(self,empleado):
        with open(self.dir,"a",newline="") as f:
            csv.writer(f).writerow([empleado.nombre,empleado.edad,empleado.salario,empleado.departamento])
    
    def buscar_empleado(self,nombre):
        with open(self.dir,"r") as f:
            for e in csv.reader(f):
                if e[0]==nombre:
                    return Empleado(e[0],int(e[1]),float(e[2]),e[3])
    
    def empleados_departamento(self,departamento):
        """with open(self.dir,"r") as f:
            datos=list(csv.DictReader(f))
            return [Empleado(e["empleado"],int(e["edad"]),float(e["salario"]),e["departamento"]) for e in datos if e["departamento"]==departamento]"""        
        # Antonio recomienda usar la funcionn vars() para enviar diccionarios a la tabla
        #este with y return lo he hecho con IA por que el de arriba original de Antonio, no iba (no hacia diccionarios).
        with open(self.dir, "r", newline="", encoding="utf-8") as f:
            lector = csv.reader(f)
            empleados = []
            for fila in lector:
                if len(fila) >= 4 and fila[3] == departamento:
                    empleados.append({
                        "Nombre": fila[0],
                        "Edad": int(fila[1]),
                        "Salario": float(fila[2]),
                        "Departamento": fila[3],
                    })
            return empleados

def general_filtrado(valor):
        with open("../11-12-2026/empleados.csv","r") as archivo:
            lector = csv.reader(archivo)
            next(lector)  # Saltar encabezados
            return list(set(e[3] for e in lector))