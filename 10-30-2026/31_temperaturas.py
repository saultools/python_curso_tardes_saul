#cual es la temperatura más baja?
temperaturas="12.4,23.6,17.8,3.5,29.0,11.6"

#solución de Saúl: (mal)
print(f"la temperatura más baja es {min(temperaturas.split(","))}")
print(temperaturas.split(","))
print(type(temperaturas))
print(20*"-")

#solución de Antonio.
print("La temperatura más baja es",min([float (t) for t in temperaturas.split(",")]))