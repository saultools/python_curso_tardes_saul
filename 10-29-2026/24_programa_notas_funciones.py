"""
Al iniciar el programa, se ebe mostraar el siguiente menú:

1. Añadir nota
2. Mostrar notas extremas (min y max)
3. Total de aprobados
4. Nota media
5. Mostrar todas las notas de la lista
6. Salir

El usuario elige una opción (1-6) y el programa le pide los datos necesarios para llevar a cabo esa acción.
Después, vueve a salir el menú y así hasta que elija la opción de salir.
"""
#solución de Saúl (funciona mal, se pilla en algunos)
notas=[]
suma=0
total=0
seleccion=0

while seleccion!=6:
    print(f"1. Añadir nota")
    print(f"2. Mostrar notas extremas (min y max)")
    print(f"3. Total de aprobados")
    print(f"4. Nota media")
    print(f"5. Mostrar todas las notas de la lista")
    print(f"6. Salir")
    seleccion=int(input("Seleccione una opción del 1 al 6:"))
    if seleccion==1:
        notas.append(int(input("Añadir nueva nota: ")))
        total=total+1
        suma=suma+notas
    elif seleccion==2:
        if notas!=[]: 
            print(f"la notas más baja es {min(notas)} y la más alta es {max(notas)}")
    elif seleccion==3:
        for total in notas:
            if total>5:
                total+=1
            print(f"hay {total} de aprobados en la lista de notas")
    elif seleccion==4:
            print(f"la media es: {suma/total}")
    elif seleccion==5:
        print(notas)
    else:
        print("por favor, añada un número del 1-6")
else:
    print("adios.")


#Solución de Antonio:
print(20*"-")

notas=[]
opcion_elegida=0
while opcion_elegida!=6 :
    print("1.- Añadir nota")
    print("2.- Mostrar notas extremas")
    print("3.- Total de aprobados")
    print("4.- Nota media")
    print("5.- Mostrar todas")
    print("6.- Salir")
    opcion_elegida=int(input("Elige opción: "))
    match opcion_elegida:
        case 1:
            notas.append(int(input("Introduce nota ")))
        case 2:
            print(f"nota más alta {max(notas)}")
            print(f"nota más baja {min(notas)}")
        case 3:
            aprobados=0
            for nota in notas:
                if nota>=5:
                    aprobados+=1
            print(f"total de aprobados {aprobados}")
        case 4:
            suma=0
            for nota in notas:
                suma+=nota
            if(len(notas)==0):
                print("No hay notas")
            else:
                print(f"nota media {suma/len(notas)}")
        case 5:
            print(notas)
        case 6:
            print("Fin del programa!")
        case _:
            print("opción no válida")