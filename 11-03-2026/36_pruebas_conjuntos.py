dia=(input("dime un día de la semana: "))
dias={"lunes","martes","miércoles"}

if dia in dias:
    print("ese dia ya existe")
else:
    dias.add(dia)
print(dias)
lista_dias=list(dias)
print(lista_dias)
print(20*".")

lista_numeros=[2,6,5,23,4,5,66,-6,-8]
conjunto_numeros=set(lista_numeros)
print(conjunto_numeros)

