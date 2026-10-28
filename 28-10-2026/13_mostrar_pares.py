""" Realiza un programa que solicite la introducción de un número
    Después, muestra todos los pares entre 1 y ese número 
"""

num_a=int(input("Introduce un número: "))

for n in range(1,num_a+1):
    if n%2==0:
        print(n, " es par")
