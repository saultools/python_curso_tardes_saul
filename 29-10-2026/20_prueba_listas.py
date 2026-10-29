# demostración directa de Antonio, no ejercicio.
lista=[4,1,8,2,11]
#muestra cada número de la lista
for num in lista:
    print(num)


# Ejercicio de Antonio:
# Muestra cada número PAR de la lista

#solución de Saúl: (correcta a la primera, yay!)
print(10*"-")
lista=[4,1,8,2,11]
for num in lista:
    if num %2==0:
        print(num)

# segundo ejercicio de Antonio: 
# Sustituye cada elemento de la lista por su cuadrado y luego imprimes la lista entera, más la suma de todo su contenido

#solución  de Saúl: (mal)
"""
print(10*"-")
for num in lista:
    lista.append(num**2)
    print(lista)
"""

#primera solución de Antonio:
print(10*"-")
lista=[4,1,8,2,11] 
indice=0
for num in lista:
    lista[indice]=num*num
    indice=indice+1
print(lista)
suma=0
for num in lista:
    suma+=num
print(f"la suma de los datos de la lista {lista} es {suma}")

#segunda solución de Antonio:
print(10*"-")
lista=[4,1,8,2,11]
for indice,num in enumerate(lista):
    lista[indice]=num*num
    indice=indice+1
print(lista)
suma=0
for num in lista:
    suma+=num
print(f"la suma de los datos de la lista {lista} es {suma}")

