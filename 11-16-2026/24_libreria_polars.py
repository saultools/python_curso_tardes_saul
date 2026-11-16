import polars as pl

datos = [ 
{"nombre": "Ana", "edad": 25, "salario": 25000,"departamento": "ventas"}, 
{"nombre": "Luis", "edad": 32, "salario": 32000,"departamento": "informática"}, 
{"nombre": "Marta", "edad": 28, "salario": 28000,"departamento": "RRHH"}, 
{"nombre": "Pedro", "edad": 41, "salario": 41000,"departamento": "ventas"}
] 
df = pl.DataFrame(datos) 
print(df) 


print(df["edad"].to_list()) # sacar columnas
print(df.row(0)) # sacar filas basado en índice: lista
print(df.row(0,named=True)) # sacar filas basado en índice: diccionario
print(df.to_dicts()) # convierte el dataframe entero en una lista de diccionarios
print(df.filter(pl.col("salario")>29999)) #filtra condicionalmente por condición dada
print(df.filter( (pl.col("salario")>26999) & (pl.col("edad")<30) )) #filtra condicionalmente por múltiples condiciones dadas
print(df.sort(by="edad",descending=False)) # ordena ascendente/descendente por columna elegida
print(df.sort("salario",descending=True.row # ordena pro salario
              (0)[0])) # y de el frame, coge la posición 0,0 (base cero)  

#min(),max(),mean(),count(),unique()
print("salario más alto: ",df["salario"].max())
print("salario más bajo: ",df["salario"].mim())
resultado = df.select(pl.col("salario").mean().alias("salario medio"),
                    (pl.col("edad").mean().alias("media de edad")))
print(resultado)

print(df["departamento"].unique().to_list())