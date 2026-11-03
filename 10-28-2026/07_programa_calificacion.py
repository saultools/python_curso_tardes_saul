#Lee la nota de un alumno y dependiendo del número (0-10)
#Le indica si es suspenso (>5), aprobado (5/6), notable (7/8), o sobresaliente (9/10).

#solución de Saúl
num=int(input("Introduce un nota:"))
if num<5:
    print("Suspenso")
elif num>=5 and num<6:
    print("Aprobado")
elif num>=7 and num<8:
    print("Notable")
elif num>=9 and num<10:
    print("Sobresaliente")
elif num>10:
    print("nota no puede ser mayor de 10")
else:
    print("por favor consulte con su profesor")

#solucion de Antonio
nota=int(input("Introduce un nota:"))
match nota:
    case 0|1|2|3|4:
         print("Suspenso")
    case 5|6:
         print("Aprobado")
    case 7|8:
         print("Notable")
    case 8|9:
         print("Sobresaliente")
    case _:
        print("Nota no válida") 