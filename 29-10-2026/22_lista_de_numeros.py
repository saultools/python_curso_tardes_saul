""" 
Solicitar la introducción de números, uno a uno, y los guardamos en una lista.
Después de pedir un número, pregunta si quiere introducir otro: sice que dice sí(S/s), 
pide uno nuevo y así sucesivamnte hasta que diga que no (N/n).
Al final, muestra la lista copleta.
"""
#solución de Saúl (funciona pero no acepta bien las excepciones...)
datos=[]

resp="s"
try:
    while resp=="s" or resp=="S":
        datos.append(input("introduce un número: "))
        resp=input("¿Desea introducir otro número(s/n)? ")
except ValueError:
    print(f"valor erróneo, por favor use S/N o s/N")
else: print(f"la lista es: {datos}")

#solución de Antonio:
resp="s"
lista=[]
while resp=="s" or resp=="S":
    try:
        num=int(input("Escribe un número "))
        lista.append(num)
        resp=input("¿Desea introducir otro número(s/n)? ")
    except ValueError:
        print("No es un valor numérico, vuelve a intentar")
    except EOFError:
        print("Error de lectura")
        break    
print(f"La lista es: {lista}") 

#solución de Antonio:
resp="s"
lista=[]
while resp=="s" or resp=="S":
    try:
        num=int(input("Escribe un número "))
        lista.append(num)
        resp=input("¿Desea introducir otro número(s/n)? ")
    except ValueError:
        print("No es un valor numérico, vuelve a intentar")
    except EOFError:
        print("Error de lectura")
        break    
print(f"La lista es: {lista}")