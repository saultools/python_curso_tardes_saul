#Ejercicio para casa: con el csv 5: basado en el presuspuesto, dar las casas que se puede permitir el usuario

import csv

lista_pres=[]
presupuesto=int(input("Introduce tu presupuesto: "))
with open("05_houses.csv","r") as f:
    row=csv.DictReader(f)
    for casa in row:
        if int(casa["price"]) <= presupuesto:
            print(f"casa que entra en tu presuspuesto: {casa}")
