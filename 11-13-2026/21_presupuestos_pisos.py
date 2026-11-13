"""A partir de houses.csv:
1. Se solicita un presupuesto y te muestra los datos de los pisos que puedes comprar,
ordenados de mayor a menor precio.
"""
import pandas as pd
filepath="../11-05-2026 - ejercicios_persistencia_datos/105_houses.csv"
df=pd.read_csv(filepath)
print(df.query("price<=@presupuesto").sort_values(by=["price"],ascending=False))