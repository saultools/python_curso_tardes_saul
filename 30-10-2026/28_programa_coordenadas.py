#Ejercicio 1:
#Solicitar al usuario la introducción de unas coordenadas (x,y),
#cada pareja de coordenadas se guarda en una lista. 
#Cada vez que solicitamos coordenadas
#preguntamos si quiere introducir nuevas coordenadas. 
#En caso afirmativo, se solicitan de nuevo
#si responde que no, finaliza el programa mostrando la lista de coordenadas

#solución de Saúl (casi correcta, solo 1 línea mal)
list_coor=[]
siono="s"
while siono=="S" or siono=="s":
    try:
        x=int(input("introduce coordenada X: "))
        y=int(input("introduce coordenada y: "))
        list_coor.append((x,y))
        # siono(input("quiere introducir más coordenadas?: (s/n)")) mal escrito por saul
        siono=input("quiere introducir más coordenadas?: (s/n)") #bien hecho por Antonio
    except ValueError:
        print("quiere introducir más coordenadas?: (s/n)")
print(f"Gracias. Sus coordenadas introducidas son: {list_coor}.")
print(20*"-")


