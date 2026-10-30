# 

def sumatorio(x,y,z=0,w=0):
    return x+y+z+w

print(sumatorio(6,5))
print(sumatorio(6,5,4))
print(sumatorio(6,5,4,9))

def sumatorio2(*args): # *args crea una lista vacía en la que podemos meter cualquier cosa.
    suma=0
    for n in args:
        suma+=n
    return suma
print(sumatorio2(5,7,84,444556.7,55,-422222)) # cualquier cosa.