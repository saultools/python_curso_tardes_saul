# Demostración de Antonio:

import csv

"""
with open("04_empleados.csv") as f:
    datos=csv.reader(f,delimiter=",") #la funcion csv.reader te escupe cada linea csv como una lista, con la primera lista/línea, con las claves.
    for row in datos:
        print(row)
print(20*"-")

with open("04_empleados.csv","r") as f:
    datos=csv.DictReader(f)  # la función csv.DictReader, escupe los objetos Json suletos
    for row in datos:
        print(row)
print(20*"-")

with open("04_empleados.csv","r") as f:
    datos=list(csv.DictReader(f)) #la función list, te crea una lista con los diccionarios json dentro
    print(datos)
print(20*"-")
"""

# EJERCICIO: (Solución de Antonio)
# soliciata la introducción de un departamento
# los nombres de las personas de ese deprtamento

dep=input("Introduce el departamento: ")
with open("04_empleados.csv","r") as f:
    datos=csv.DictReader(f) # la función csv.DictReader, escupe los objetos Json suletos
    for emp in datos:
        if emp["departamento"]==dep:
            print(emp["empleado"])
print(20*"-")

#nombre del empleado con mayor salario
empleado_mas_salario=()

with open("04_empleados.csv","r") as f:
    datos=list(csv.DictReader(f))
    empleado_max=max(datos,key=lambda x:x["salario"])
    print(f"empleado {empleado_max["empleado"]} gana {empleado_max["salario"]}")