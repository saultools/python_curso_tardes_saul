import calculadora_03 as calc

y = calc.CALCULADORA
z = calc.CALCULADORA

y = float(input("introduce número a: "))
z = float(input("introduce número b: "))
operadores = calc.CALCULADORA(y,z)

print(f"suma: {operadores.sumar()}")
print(f"resta: {operadores.restar()}")
print(f"multiplicar: {operadores.multiplicar()}")
print(f"dividir: {operadores.dividir()}")