#Ejercicio de Antonio: lista de reproducción
#Se solicita la introducción de los datos de una nueva canción.
#y se agrega a la lista
#Después, el programa muestra todos los titulos almacenados
#y la valoración media de toda la lista de reproducción 
lista_reproduccion=[
    {"titulo":"canción inventada","duracion":3.20,"valoracion":4},
    {"titulo":"Bohemian Rapsody","duracion":5.40,"valoracion":10},
    {"titulo":"Green summer","duracion":4.10,"valoracion":7}
]

#solución 1 de Saúl:
"""
print("Agregador de canciones")
lista_reproduccion["titulo"]=input("Introduce título: ")
lista_reproduccion["duracion"]=float(input("Introduce duración: "))
lista_reproduccion["titulo"]=int(input("Introduce valoración 1-10: "))
print(lista_reproduccion)
print(f"valoración media de la lista de reproducción: ")
"""
#tip de Antonio: crea unnuevo diccionario, LUEGO añádelo a a la lista de diccionarios + solución a lo de medias
print("Agregador de canciones")
titulo=input("Introduce título: ")
duracion=float(input("Introduce duración: "))
valoracion=int(input("Introduce valoración 1-10: "))
cancion_nueva={"titulo":titulo,"duracion":duracion,"valoracion":valoracion}
lista_reproduccion.append(cancion_nueva)
print(lista_reproduccion)

suma=0
for c in lista_reproduccion:
    suma+=c["valoracion"]
    print(c["titulo"])
print(f"valoración media de la lista de reproducción: {suma/len(lista_reproduccion)}")
print(20*"-")


#nuevo ejercicio:
#Se solicita la introducción de los datos de una nueva canción.
#si la canción no existe, se agrega a la lista. Si ya existe no se hace nada
#Después, el programa muestra todos los titulos almacenados 
# y la valoración media de toda la lista de reproducción

#solución de Saúl fallida - solucionada por Antonio en la pantalla
lista_reproduccion_2=[
    {"titulo":"canción inventada","duracion":3.20,"valoracion":4},
    {"titulo":"Bohemian Rapsody","duracion":5.40,"valoracion":10},
    {"titulo":"Green summer","duracion":4.10,"valoracion":7}
]

titulo=input("Introduce el título de la canción:")
duracion=float(input("Introduce la duración de la canción:"))
valoracion=int(input("Introduce valoración de la canción:"))
cancion_nueva={"titulo":titulo,"duracion":duracion,"valoracion":valoracion}

def title_check(titulo):
    return titulo in [can["titulo"] for can in lista_reproduccion_2]
    #este comentario es otra manera de hacer lo mismo que en la lista comprimida de arriba, pero en compresión de listas es más elegante.
    """ 
    for item in lista_reproduccion_2:
            if item["titulo"]==titulo:
                return True
        return False #si llega aquí es por que no ha hecho match el título.
    """

if not title_check(titulo):
    lista_reproduccion_2.append(cancion_nueva)
else:
    print("La canción no fue añadida")
suma=0

for c in lista_reproduccion_2:
    suma+=c["valoracion"]
    print(c["titulo"])
print(f"Valoración media {suma/len(lista_reproduccion_2)}")
