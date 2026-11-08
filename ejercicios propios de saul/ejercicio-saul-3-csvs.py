import csv
dirfile="../11-05-2026 - ejercicios_persistencia_datos/04_empleados.csv"

with open(dirfile) as f:
    datos=csv.reader(f,delimiter=",") # csv.reader te escupe cada linea csv como una lista, con la primera lista/línea, con las claves.
    for row in datos:
        print(row)
print(20*"-")

with open(dirfile,"r") as f:
    datos=csv.DictReader(f)  # csv.DictReader, escupe los objetos Diccionario/Json suletos
    for row in datos:
        print(row)
print(20*"-")

with open(dirfile,"r") as f:
    datos=list(csv.DictReader(f)) # fun=list(csv.Dictreader(iterador_del_with)) crea una lista con los diccionarios json dentro
    print(datos)
print(20*"-")


