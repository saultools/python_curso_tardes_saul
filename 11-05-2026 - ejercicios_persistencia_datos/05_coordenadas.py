#calcula la distancia más corta entre coordenadas del csv 06

"""solución de Saúl (sin terminar)
import math
import csv

def distancia(p1,p2):
   return math.hypot(p1[0]-p2[0],p1[1]-p2[1]) 

dists=[]
with open("05_coordenadas.csv","r") as f:
    rows=csv.reader(f)
    for value in rows:
        if value is str:
            next()
        else:
            float(value["x"])
            float(value["y"])
            x=value["x"]
            y=value("y")
            dists.append(x,y)
print(dists)
# print(f"la menor distancia entre puntos es {min(dists)}")
"""

#solución de Antonio:
import math
import csv

def distancia(punto1,punto2):
   return math.dist(punto1,punto2)
   return math.hypot(punto1[0]-punto2[0],punto1[1]-punto2[1]) 

pos_usuario=(int(input("Tu posición x: ")),int(input("Tu posición y: ")))
dir_fichero="05_coordenadas.csv"
#En esta variable se obtendrá la distnacia más corta
distancia_corta=None
#En esta variable se deberá obtener la tupla de la tienda más cercana
coordenada_tienda=None
with open(dir_fichero,"r") as f:
    coordenadas=csv.DictReader(f)
    for row in coordenadas:
        coord=(int(row["x"]),int(row["y"]))
        if distancia_corta==None: #es la primera vez
            distancia_corta=distancia(coord,pos_usuario)

        if coordenada_tienda==None:
            coordenada_tienda=coord

        dist=distancia(coord,pos_usuario)
        if dist<distancia_corta:
            distancia_corta,coordenada_tienda=dist,coord

print(f"La tienda mas cercana a {pos_usuario} tiene de coordenadas {coordenada_tienda}") 

#solución 2 de Antonio:
with open(dir_fichero,"r") as f:
    next(f)
    coordenadas=list(csv.reader(f))
    coordenada_tienda=min(coordenadas,key=lambda c:distancia(int((c[0]),int(c[1])),pos_usuario))
print(f"La tienda mas cercana a {pos_usuario} tiene de coordenadas {coordenada_tienda}") 