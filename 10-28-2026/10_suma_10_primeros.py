#hacer un programa que muestre la suma de los 10 primeros números naturales (del 1 al 10)

suma=0

for n in range(1,11):
    suma=suma+n
print(suma)

# y también todos los números naturales y un número leído por teclado

num_teclado=int(input("introduce un número para tu suma "))

for n in range(1,11):
    suma=suma+n+num_teclado
print(suma)