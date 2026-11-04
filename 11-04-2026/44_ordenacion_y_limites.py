lista=[5,2,11,6,44,20,1]
lista_ordenada=sorted(lista) #nueva lista ordenada
lista_ordenada_al_reves=sorted(lista,reverse=True) #nueva lista ordenada al revés
print(lista_ordenada_al_reves)

nombres=["bicicleta","oro","casa","martillo"]
print(sorted(nombres))

print(f"sorted by charachter lenght {sorted(nombres,key=lambda e:len(e))}") # key es una función de sorted: la función que quieras

#de la lista de números, imprime el mayor, y el menor
print(max(lista))
print(min(lista)) #max y min son funciones hijas de sorted(): por lo tanto también pueden aceptar key=funciones
#imprime el que tiene menos caracteres
print(min(nombres,key=lambda e:len(e)))
