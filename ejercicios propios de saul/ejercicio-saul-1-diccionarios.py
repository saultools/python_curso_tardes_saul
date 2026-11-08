ciudades = {"Madrid": 27.3, "Sevilla": 33.5, "Soria": 19.5}
ciudanombres=list(ciudades) # convierte el dicconario en una lista de los nombres de las claves.
print(ciudanombres)

print(f"en {ciudanombres[0]}, la temperatura es {ciudades["Madrid"]}\n")

ciudades["Sevilla"] = 31.7       # modifica
ciudades["Salamanca"] = 22.4     # añade
del ciudades["Madrid"]            # elimina

print("resto de ciudades:")
for k, v in ciudades.items(): # loop para imprimir un diccionario
    print(k, v)
print()

d = {'name': 'John', 'age': 25, 'city': 'New York'}
a = list(d.keys())
b = list(d.values())
print(a)
print(b)
print()

dl = [
    {'name': 'John', 'age': 25, 'city': 'New York'},
    {'name': 'Alice', 'age': 30, 'city': 'London'},
    {'name': 'Carlos', 'age': 22, 'city': 'Madrid'},
    {'name': 'Yuki', 'age': 28, 'city': 'Tokyo'},
    {'name': 'Emma', 'age': 35, 'city': 'Berlin'},
    {'name': 'Liam', 'age': 19, 'city': 'Dublin'},
    {'name': 'Sofia', 'age': 27, 'city': 'Rome'},
    {'name': 'Lucas', 'age': 40, 'city': 'São Paulo'},
    {'name': 'Amira', 'age': 31, 'city': 'Cairo'},
    {'name': 'Chen', 'age': 24, 'city': 'Beijing'},
    {'name': 'Olivia', 'age': 26, 'city': 'Sydney'},
]
for dict_item in dl:
    print(f"Nombre: {dict_item["name"]}, Edad: {dict_item["age"]}, Ciudad: {dict_item["city"]}")

print()
alumnos = [
  {"nombre": "Ana",  "notas": [7, 9, 10]},
  {"nombre": "Luis", "notas": [5, 6, 8]},
]
print(alumnos[0:]) 
print(alumnos[1]["nombre"], alumnos[1]["notas"][2])
for al in alumnos:
    print(f"nota media de {al["nombre"]}: {sum(al["notas"])/len(al["notas"])}")

print()
tienda = {"frutas": ["pera", "uva"], "precios": (1.2, 2.5)}
print(tienda["precios"][1])        # 2.5  (precio de la uva)