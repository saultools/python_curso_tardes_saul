#Solicitamos al usuario que introduzca un lenguaje que quiera aprender, 
#y le mostramos todos los cursos relacionados con ese lenguaje
cursos="Java basic, Python principiantes, C, Java avanzado, Java enterprise, python web, cobol"

#solución de Saúl:
lista_cursos=cursos.split(",")
lenguaje=input("Qúe lenguaje te interesa?: ")
if lenguaje.lower() in lista_cursos:
    print(f"{lenguaje} está en la lista")

print(20*"-")

#solución de Antonio:
lista_cursos=cursos.split(",")
lenguaje=input("Que lenguaje te interesa?")
for c in lista_cursos:
    if lenguaje.lower() in c.lower().split(" "):
        print(c)