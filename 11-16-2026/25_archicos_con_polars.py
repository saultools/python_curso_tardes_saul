import polars as pl

filepath="../11-05-2026 - ejercicios_persistencia_datos/105_houses.csv"
df=pl.scan_csv(filepath)

filtro = df.filter(pl.col("rooms")>3)