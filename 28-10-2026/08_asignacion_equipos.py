# Teniendo en cuenta que alevín es 10 años y benjamín es 16:
# Hacer un programa que solicite la edad y nos muestre a que grupo pertenece (el más ccercano a su edad). 
# La edad debe estar ente 9 y 18 años.

#solución de Saúl primera
edad=int(input("Introduce tu edad "))

if edad>=9 and edad<=13:
    print("Alevín")
elif edad>=13 and edad<=18:
    print("Benjamín")
elif edad>9 or edad<18:
    print("Fuera de rango de edad")

#tip de Antonio
limite_inf,limite_sup,benjamin,alevin=9,18,10,16

#solución de Saúl segunda (mal, por que no funciona para los 13 años)
if edad>=alevin and edad<=benjamin:
    print("Alevín")
elif edad>=benjamin and edad<=limite_sup:
    print("Benjamín")
elif edad<limite_inf or edad>limite_sup:
    print("Fuera de rango de edad")

#solución de Antonio
if edad<limite_inf or edad>limite_sup:
    print("La edad no es válida")
else:
    distancia_benjamin=edad-benjamin
    distancia_alevin=edad-benjamin
    if distancia_benjamin<distancia_alevin:
        print("Eres benjamín")
    else:
        print("Eres alevín")
