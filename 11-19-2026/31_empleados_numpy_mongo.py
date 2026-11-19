""" A partir de la colección de la base de datos (local, en MongoDB "empresa"), calcular:
1. salario medio e todos los empleados
2. Edad mayor
3. Lista de departamentos
"""
#juegos de saul
import numpy as np, pymongo as pm
"""
url="mongodb://localhost:27017"
serv=pm.MongoClient(url)

empleados = serv.empresa.empleados
datos = list(empleados.find())
serv.close()
for n in datos:
    print(n)
print()
print(datos[0])
"""

#solución de Antonio
def crear_conexion():
    url="mongodb://localhost:27017"
    return pm.MongoClient(url)

serv=crear_conexion()
col_empleados=serv.empresa.empleados
datos=list(col_empleados.find())
serv.close()
print(datos)

salarios=np.array([e["salario"] for e in datos])
edades=np.array([e["edad"] for e in datos])
departamentos=np.array([e["departamento"] for e in datos])

print(f"Salario medio: {np.average(salarios)}")
print(f"Edad mayor: {np.amax(edades)}")
print(f"Departamentos: {np.unique(departamentos)}") 