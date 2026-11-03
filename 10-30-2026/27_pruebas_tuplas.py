#crea una tupla con los cinco primeros números
numeros=(1,2,3,4,5)


#leer el nombre y apellido de una persona y guardalo en una tupla
nombre=input("Nombre: ")
apellido=input("Apellidos: ")

datos=(nombre,apellido)
print(datos)

#demostración: Las funciones len, max y min también son aplicables en tuplas
lista=[3,9,1,7,11]
mtup=tuple(lista)
print(len(mtup)) #5
print(max(mtup)) #11
print(min(mtup)) #1

#demostración: La función tuple permite convertir una lista en una tupla:
lista=[3,9,1,7,11]
mtup=tuple(lista)