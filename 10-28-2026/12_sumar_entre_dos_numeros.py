# Solicita la introducción de dos números 
# y calcula la suma de todos los números 
# comprendidos entre el mayor y el menor

#solución de Saúl primera (no funciona si el menor numero viene segundo)
num_a=int(input("Introduce un número: "))
num_b=int(input("Introduce un número: "))
suma=0
num_a,num_b=num_a,num_b+1
for n in range(num_a,num_b):
    suma=suma+n
print(f"la suma de todos los números entre los introducidos, es: ",suma)


#soluciones de Antonio
num1=int(input("Primer número "))
num2=int(input("Segundo número "))
suma=0
#solución 1
if num1<num2:
    menor,mayor=num1,num2
else:
    menor=num2
    mayor=num1
    
for n in range(menor,mayor+1):
    suma=suma+n

#solución 2
"""
if num1<num2:
    for n in range(num1,num2+1):
        suma=suma+n
else:
    for n in range(num2,num1+1):
        suma=suma+n

#solución 3
if num1>num2:
    num1,num2=num2,num1
    
for n in range(num1,num2+1):
    suma=suma+n
"""
print("La suma es ",suma)