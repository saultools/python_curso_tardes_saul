# dada esta lista de notas, crea otra lista que contenga solo los aprobados. 
# Además le añadirás un punto extra a cada uno de los aprobados. finalmente se imprime la nueva lista.

# solución de Saúl (mal)
numeros=[4,3,7,8,7,9,2]
"""
for n in enumerate(numeros):
    if n>5:
        n+=n
print(numeros)
"""

# solución de Antonio:
aprobados=[]
for nota in numeros:
    if nota>=5:
        aprobados.append(nota+1)
print(aprobados)

# solución alternativa (avanzada) de Antonio:
aprobados2=[nota+1 for nota in numeros if nota>=5] #esto se llama "compresión de listas" (filtrar listas, operar en listas...)
print(aprobados2)

#ejercicio siguiente: Crea una función que haga la misma tarea, pero que al final imprima el resultado como una tupla
def aprobados3():
    return tuple([nota+1 for nota in numeros if nota>=5])
print(aprobados3)