import polars as pl

filepath = "../11-16-2026/ventas_tiendas.csv"
df = pl.scan_csv(filepath)

def tiendas_ver():
    return df.select(pl.col(df.collect_schema().names()[0])
                     .unique()).collect().to_series().to_list()
def mes_ver():
    return df.select(pl.col(df.collect_schema().names()[1])
                     .unique()).collect().to_series().to_list()

columnascsv = df.collect_schema().names()
tiendacsv = columnascsv[0]
mescsv = columnascsv[1]

def tienda_filtrada(tienda):
    return df.filter(pl.col(tiendacsv) == tienda).collect()

def mes_filtrado(mes):
    return df.filter(pl.col(mescsv) == mes).collect() 


# solución de medias de compañero Luis Enrique
def datos_tienda(tienda):
    return df.filter(pl.col("nombre_tienda") == tienda)

def total_facturacion(tienda):
    return datos_tienda(tienda).select("facturacion").sum().row(0)[0]

def total_gasto_personal(tienda):
    return datos_tienda(tienda).select("gastos_personal").sum().row(0)[0]

def mes_mayor_facturacion(tienda):
    return datos_tienda(tienda).sort(by="gastos_personal", descending=True).row(0)


def datos_tiendas(mes):
    return df.filter(pl.col("mes") == mes)

def media_facturacion(mes):
    return datos_tiendas(mes).select("facturacion").mean().row(0)[0]

def mayor_gasto_personal(mes):
    return datos_tiendas(mes).sort(
        by="gastos_personal",descending=True).select(
            "nombre_tienda","gastos_personal").row(0) 