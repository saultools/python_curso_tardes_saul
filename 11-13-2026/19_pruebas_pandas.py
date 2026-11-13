import pandas as pd

lista_reproduccion=[
    {"titulo":"canción inventada","duracion":3.20,"valoracion":4},
    {"titulo":"Bohemian Rapsody","duracion":5.40,"valoracion":10},
    {"titulo":"Green summer","duracion":4.10,"valoracion":7}
] 
df=pd.DataFrame(lista_reproduccion) # crea un dataframe de pandas a partir de la lista
print(df)

datos=[{"nombre":"paco","edad":20},
       {"nombre":"ana","edad":45},
       {"nombre":"maria","edad":30},
       {"nombre":"laura","edad":32}]
df2=pd.DataFrame(datos)
print(df2)

empleados="../12-11-2026/empleados.csv"
df3=pd.read_csv(empleados)
#df3.index=df3["edad"]
print(df3)

"""print(df)
print(df.columns)
print(df.values)"""

for v in df.values:
    print(v[0])
#salario medio
print(f"salario medio: {df["salario"].mean():.2f}")
print(f"salario medio de informática: {df.query("departamento=='informática'")["salario"].mean():.2f}")

#Quiero agruparlos por departamento y con la columna salario medio y edad máxima
grupo=df.groupby("departamento").agg(salario_medio=("salario","mean"),edad_maxima=("edad","max"))
print(grupo.sort_values(by=["salario_medio","edad_maxima"])) 