#pregunta al usuario que lenguaje quiere aprender, y el programa le indicará 
# si el curso existe para ese lenguajo o no

#solucion de Saúl:
cursos=["Java","Python","Typescript","C","Dart"]

intencion=input("Qué lenguaje de programación quieres aprender: ")
if intencion.lower() in cursos:
    print("si hay")
else:
    print("no hay")
print(20*"-")

#solución de Antonio: (que recorre toda la lista para cada búsqueda)
if intencion.lower() in [c.lower() for c in cursos]:
   print("Tengo ese curso!")
else:
   print("Lo siento, no tengo ese curso") 