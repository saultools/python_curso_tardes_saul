#Solicitamos al usuario que introduzca un lenguaje que quiera aprender, 
#y le mostramos todos los cursos relacionados con ese lenguaje
cursos="Java basic, Python principiantes, C, Java avanzado, Java enterprise, python web, cobol"

#solución de Saúl:
lista_cursos=cursos.split(",")
lenguaje=input("Qúe lenguaje te interesa?: ")
if lenguaje.lower() in lista_cursos:
    print(f"{lenguaje} está en la lista")
else:
    print(f"{lenguaje} NO está en la lista")

#solución de Antonio:
