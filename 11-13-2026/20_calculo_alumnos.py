""" Usando pandas y alumnos.json (../12-11-2026), realizar:
1. Calcular la  nota media global
2. Mostrar la nota más alta del cada curso
3. Mostrar el total de alumnos de cada curso 
"""
import pandas as pd
filepath = "../11-06-2026/06_alumnos.json"
df=pd.read_json(filepath)

print(f"Nota media global: {df["nota"].mean():.2f}")
grupo=df.groupby("curso").agg(nota_mayor=("nota","max"),total_alumnos=("nombre","count"))
print(grupo) 
