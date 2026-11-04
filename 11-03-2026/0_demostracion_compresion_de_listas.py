numeros=[3,-1,-9,4,2,11,-8,7,-5]
#CREA UNA LISTA A PARTIR DE LA ANTERIOR QUE CONTENGA SOLO LOS POSITIVOS

#sin compresión de listas:
positivos=[]
for n in numeros:
    if n>=0:
        positivos.append(numeros)
print(positivos)

#con compresión de listas:
positivos_c=[n for n in numeros] #esto sería un duplicado exacto de numeros lista
positivos_c=[n for n in numeros if n>=0] #metiendo el if después de la lista duplicada, te "ahorras" el tenr que poner el append
positivos_c=[n for n in numeros if n%2==0] #otro ejemplo de filtrado fon if.
positivos_c=[n+5 for n in numeros if n>=0] #así operas a la lista, y luego pones el filtro del ip a la lista ya operada

print(positivos_c)

#indica si hay algún número par en la lista

if [n for n in numeros if n%2==0]:
    print("hay algún par")
else:
    print("no hay par")