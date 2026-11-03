#definiendo variables num1 y num2 como input fields
num1=input("Introduce primer número: ")
num2=input("Introduce segundo número: ")

#convirtiendo los inputs a integrales
num1=int(num1)
num2=int(num2)

#definiendo posibles operaciones
suma=num1+num2

# generando operaciones para el usuario
print(f"la suma de {num1} y {num2} es {suma}")
print(f"la resta de {num1} y {num2} es {num1-num2}")
print(f"la multiplicación de {num1} y {num2} es {num1*num2}")
print(f" la división de {num1} y {num2} es {num1/num2}")