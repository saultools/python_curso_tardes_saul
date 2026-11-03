# Realiza un programa que solicite la introducción de un número,
# y calcule su factorial

#ejercicio de saul (mal)
numero=input("Introduce un número ")
factorial=1
for n in range(2,limite+1):
    factorial=factorial*numero
print(f"El factorial de {limite} es: ",factorial)


#solucion del ejercicio de Antonio
#REalizar un programa que solicite la introdución de un número
#y calcule su factorial    7!  7*6*5*4*3*2*1
factorial=1
limite=int(input("Introduce límite "))
for num in range(2,limite+1):
    factorial=factorial*num
print(f"El factorial de {limite} es: ",factorial) 