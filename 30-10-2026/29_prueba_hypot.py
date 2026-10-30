#demostración de función hypot.
from math import hypot
punto1=(3,4)
punto2=(7,6)
distancia=hypot(7-3,6-4) 
print(distancia)



# basada en la lista del ejercicio 28: Se pide al usuario su posición, después el programa (de petición de coordenadas).
# Se le mostrará las coordenadas del punto más cercano (de la lista) a su posición.

#solución de Saúl (incompleta, mal)
siono="s"
print("Busquemos las tiendas mas cercanas a su localzación")

tiendas=[]
while True:
    try:
        x=int(input("introduce coordenada X de tienda: "))
        y=int(input("introduce coordenada Y de tienda: "))
        tiendas.append((x,y))
        print(tiendas)
    except ValueError:
        print("bix usa numeros")
        break
seguir = input("¿Quiere introducir más coordenadas? (s/n): ").strip().lower()
 
  
while True:
    try:
        v=int(input("introduce tu coordenada X: "))
        w=int(input("introduce tu coordenada Y: "))
        c_usuario=[v,y]
        print(c_usuario)
    except ValueError:
        print("bix usa numeros!")
    break

""" esta parte de mi solución está mal
for n in tiendas:
    distancia=hypot(c_usuario(0),n(0),c_usuario(1),n(1))
"""

#y antonio lo soluciona así:
def distancia(p1, p2):
    """Devuelve la distancia euclídea entre p1 y p2."""
    return hypot(p1[0]-p2[0],p1[1]-p2[1])

print(f"tu distancia a la tienda más cercana es: {distancia}")
print(20*"-")



#solución de Antonio:
coordenadas=[]
def distancia(punto1,punto2):
   return hypot(punto1[0]-punto2[0],punto1[1]-punto2[1]) 
resp="S"
while resp=="S" or resp=="s":
    x=int(input("X de la tienda: "))
    y=int(input("Y de la tienda: "))
    coordenadas.append((x,y))
    resp=input("¿Quiere introducir nuevas coordenadas (S/N)?")
print(coordenadas)
#Se pide al usuario su posición, después el programa
#le mostrará las coordenadas del punto 
#más cercano a su posición

pos_usuario=(int(input("Tu posición x: ")),int(input("Tu posición y: ")))
#En esta variable se obtendrá la distnacia más corta
distancia_corta=distancia(coordenadas[0],pos_usuario)
#En esta variable se deberá obtener la tupla de la tienda más cercana
coordenada_tienda=coordenadas[0]
#recorremos las coordenadas y para cada una de ellas,
#obtenemos la distancia con la posición del usuario. Si encontramos que esa distancia
#es inferior distancia_corta, actualizamos tanto las variables distancia_corta
#como coordenada_tienda
for coord in coordenadas:
    dist=distancia(coord,pos_usuario)
    if dist<distancia_corta:
        distancia_corta,coordenada_tienda=dist,coord
print(f"La tienda mas cercana a {pos_usuario} tiene de coordenadas {coordenada_tienda}")