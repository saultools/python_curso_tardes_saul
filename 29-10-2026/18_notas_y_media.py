#solicita una nota, despues otra, y así sucesivamente hasta introducir un cero
#en ese momento, no pedirá más notas y mostrará la nota media de las introducidas 
#hasta el momento

#solución de Saúl (incompleta)
nota=[]
total_introducido=0
media_notas=0

while nota != 0:
    nota.append(int(input("Introduce un nota: ")))
    total_introducido+=1
    print(total_introducido)
    print(nota)
else:
    print(f"usted ha introducido {total_introducido} notas, que hacen una media de {media_notas}")


#solución de Antonio:
print(10*"-")

suma=0
total=0
nota=int(input("Introduce nota "))
while nota>0:
    total=total+1
    suma=suma+nota
    nota=int(input("Introduce nota"))
try:
    print(f"Has introducido {total} notas, y la media es: {suma/total}")  
except ZeroDivisionError:
    print("No hay notas")