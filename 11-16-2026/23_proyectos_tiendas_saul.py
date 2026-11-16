""" Sobre el archivo de ventas_tiendas.csv y usando la librería Pandas, realizar:
1. A partir de nombre de tienda, mostrar sus ventas totales
2. Mostrar el mayor gato de personal de tiendas
3. A partir del nombre de tienda, mes en la que esta obtuvo mayor facturación 
4. muestra la tienda más antigua
"""
import pandas as pd
filepath="./ventas_tiendas.csv"
df=pd.read_csv(filepath)

print()
print("Ventas totales por tienda, en €")
df1 = df
totales_por_tienda = df1.groupby("nombre_tienda")["facturacion"].sum()
print(totales_por_tienda)

"""
#solución de Antonio
tottienda = df
tienda = input("introduce el nombre de la tienda: ")
tottienda = tottienda.query("nombre_tienda==@tienda")
print(f"La facturación total de la tienda {tienda} es {tottienda["facturacion"].sum()}")
"""

print()
print("Tienda con más gasto (de personal) anualizado por año")
tdo = df
tdo.groupby()


print()
print("Escoja tienda para ver mes-año con mayor facturación")
maf = df
mafinput = input("introduce el nombre de la tienda: ")
maf = maf.query("nombre_tienda==@mafinput")
print(f"{mafinput} tuvo las mayores ventas: {max(maf)}")

print()
tigua = df
tigua
print("La tienda más antigua es ")