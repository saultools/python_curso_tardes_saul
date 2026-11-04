"""
Realiza un progrma para la organizacion de una libreria
un libro tiene tres propiedades: titulo, autor y precio.

Cuando se inicie el programa, se va a mostrar un menu:
1-Nuevo libro
2-Mostrar todos
3-Buscar por titulo
4-Libros por precio maximo
5-Salir

1-Se piden los datos del nuevo libro y se guardan
2-Se muestran los titulos de todos los libros
3-Se le pide el titulo y se muestran todos sus datos
4-Se le pide el precio maximo y se muestran los titulos de los libros cuyo precio sea igual o inferior al introducido
Despues de ejecutar cualquiera de las anteriores opciones, se muestra de nuevo el menu.
Asi hasta que elija la opcion 5 que sale del programa
""" 

#Solución de Saúl: FFFUUUNNCCCIIOONNA!!!!! (pero incompleto 4k no me ha dado tiempo)
libros_db=[
    {"titulo":"Serie Fundación (5 libros)",
    "autor":"Isaaac Asimov",
    "precio":65.99},
    {
    "titulo": "La Trilogía del Imperio",
    "autor": "Larry Niven",
    "precio": 62.90},
    {
    "titulo": "El Ascenso de la Civilización",
    "autor": "Greg Bear",
    "precio": 58.40},
    {
    "titulo": "El Legado de los Colonos",
    "autor": "Alastair Reynolds",
    "precio": 61.25},
    {
    "titulo": "Horizontes de la Humanidad",
    "autor": "C.J. Cherryh",
    "precio": 57.80}
]

def menu():
    print(15*"-")
    print("1.- Nuevo libro")
    print("2.- Mostrar todos")
    print("3.- Buscar por titulo")
    print("4.- Libros por precio maximo")
    print("5.- Salir")
    print(30*"-"+"\n")

opcion_elegida=0
while opcion_elegida!=5:
    try:
        menu()
        opcion_elegida=int(input("Elige opción: "))
        match opcion_elegida:
            case 1:
                titulo=input("Introduce título: ")
                autor=input("Introduce autor: ")
                precio=float(input("Introduce pecio: "))
                
                libro_nuevo={"titulo":titulo,
                            "autor":autor,
                            "precio":precio}
                libros_db.append(libro_nuevo)
            case 2:
                print(libros_db)
            case 3:
                def title_check(titulo):
                    return titulo.lower() in [tit["titulo"].lower() for tit in libros_db]
                titulo=(input("Introduce el título del libro: ").strip().lower())

                if title_check(titulo):
                    print(f"Título encontrado\n")
                    print(title_check(titulo))
                else: print("Título no encontrado.")
            case 4:
                print("opción en desarrollo.")
            case 5:
                print("Fin de la sesión.")
            case _:
                print("Opción no válida.")
    except ValueError:
        print("bix usa numeros!")

#solución de Antonio:
libros=[]
def mostrar_menu():
    print("\n--- MENÚ ---")
    print("1 - Nuevo libro")
    print("2 - Mostrar todos")
    print("3 - Buscar por título")
    print("4 - Libros por precio máximo")
    print("5 - Salir")
def titulos():
    print("Títulos de los libros:")
    for lib in libros:
        print(f"Título: {lib["titulo"]} precio:{lib["precio"]}")
def buscar_titulo(titulo):   
    encontrado=False    
    for i in libros:
        if titulo.lower() == i["titulo"].lower():
            print("Se ha encontrado tu libro")
            print(f"Título: {i['titulo']} Autor: {i['autor']} Precio: {i['precio']}")
            encontrado= True
            break
    if not encontrado:
        print("Libro no encontrado")
    return encontrado
def nuevo_libro():
	titulo = input("Título: ")
	autor = input("Autor: ")
	try:
		precio = float(input("Precio: "))
	except ValueError:
		print("Precio no válido. No se agregó el libro.")
		return
	if not buscar_titulo(titulo):
		libros.append({"titulo": titulo, "autor": autor, "precio": precio})
		print("Libro agregado.")
	else:
		print("Libro repetido, no se agregó")
def libros_por_precio_maximo(max_precio):  
    titulos = [n["titulo"] for n in libros if n["precio"]<=max_precio]    
    if len(titulos)>0:
        print(f"Libros con precio <= {max_precio}:")
        for j in titulos:
            print(j)  
    else:
        print("No hay libros con ese precio o inferior.")
opcion="0"    
while opcion!="5":
	mostrar_menu()
	opcion=input("Elige una opción: ")
	if opcion == "1":
		nuevo_libro()
	elif opcion == "2":
		titulos()
	elif opcion == "3":
		buscar=input("Introduce el titulo del libro que quieres buscar: ")
		buscar_titulo(buscar)
	elif opcion == "4":
		try:
			max_precio = float(input("Precio máximo: "))
			libros_por_precio_maximo(max_precio)
		except ValueError:
			print("Precio no válido.")
	elif opcion == "5":
		print("Saliendo del programa...")
	else:
		print("Opción no válida. Intenta de nuevo.")