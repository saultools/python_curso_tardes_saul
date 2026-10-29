# Ejercicio: Indica cuantos alumnos han aprobado
notas_alumnos=[6.4,2.9,5.5,8.0,3.1,7.2]

#Solucionado por Saúl con ayuda de la pizarra de Antonio
indice=0
for num in notas_alumnos:
    if num>5:
        indice+=1
print(f"hay {indice} aprobados")
print(10*"-")

#ejercicio nuevo: Indica la nota más alta

#solución de Saúl (terminada con las correcciones de la pizarra)
notas_alumnos=[6.4,2.9,5.5,8.0,3.1,7.2]
nota_mas_alta_aun=0

for n in notas_alumnos:
    if n>nota_mas_alta_aun:
        nota_mas_alta_aun=n
print(f"la nota mas alta es {nota_mas_alta_aun}")
print(10*"-")

#solución con función .max
print(f"la nota más alta es {max(notas_alumnos)}")

# demostración de ordenar (sort) una lista:
print(f"las notas ordenadas de menor a mayor es {sorted(notas_alumnos)}")
# demostración de ordenar (sort) una lista de más a menos:
print(f"las notas ordenadas de mayor a menor es {sorted(notas_alumnos,reverse=True)}")

#soluciones de antonio:
notas_alumnos=[6.4,2.9,5.5,8.0,3.1,7.2]
#indica cuantos alumnos han aprobado
aprobados=0
for n in notas_alumnos:
    if n>=5:
        aprobados=aprobados+1
print("El total de aprobados es ",aprobados)
#indica la nota más alta
"""
mayor=notas_alumnos[0] #inicializamos la variable con cualquiera de las notas
for nota in notas_alumnos:
    if nota>mayor:
        mayor=nota
print(f"La nota más alta es {mayor}")
"""
print(f"La nota más alta es {max(notas_alumnos)}")
print(f"La nota más baja es {min(notas_alumnos)}")
print(f"Las notas en orden son: {sorted(notas_alumnos,reverse=True)}")
