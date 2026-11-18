"""*Al seleccionar una tienda se mostrara:
Una tabla con la información de dicha tienda. Y debajo de esa tabla:
-total de facturación
-total de gastos de personal
-mes con mayor facturación

*Al seleccionar un mes se mostrará:
Una tabla con los datos de ese mes. Y debajo de esa tabla:
-Media de facturación de todas las tiendas
-Tienda con mayor gasto de personal """

#-------------------tiendas_repository.py
import polars as pl

df = pl.read_csv("../ventas_tiendas.csv")

def tiendas():
    return df["nombre_tienda"].unique().to_list()

def meses():
    return df["mes"].unique().to_list()

#----# funciones relacionadas al 1er cuadro #----#
def datos_tabla_tienda(tienda):
    return df.filter(pl.col("nombre_tienda") == tienda).to_dicts()

def datos_tienda(tienda):
    return df.filter(pl.col("nombre_tienda") == tienda).select(pl.col("facturacion").sum().alias("facturacion_total"),
                                                               pl.col("gastos_personal").sum().alias("gastos_totales")).to_dicts()
def mes_mayor_facturacion(tienda):
    return df.filter(pl.col("nombre_tienda") == tienda).sort(by="gastos_personal", descending=True).row(0)

#----# funciones relacionadas al 2do cuadro #----#
def datos_tabla_mes(mes):
    return df.filter(pl.col("mes") == mes).to_dicts()

def media_facturacion(mes):
    return df.filter(pl.col("mes") == mes).select(pl.col("facturacion").mean().alias("facturacion_media")).to_dicts()

def mayor_gasto_personal(mes):
    return df.filter(pl.col("mes") == mes).sort(by="gastos_personal", descending=True).row(0) 

#-------------------app.py

import streamlit as st
# import tiendas_repository as repo

tienda_sel=None
mes_sel=None
with st.sidebar:
    st.subheader("Filtrado de datos")
    tienda_sel=st.selectbox("Seleccione tienda",repo.tiendas(),index=None,key=1)
    mes_sel=st.selectbox("Seleccione mes",repo.meses(),index=None,key=2)
    
if tienda_sel!=None:
    st.table(repo.datos_tabla_tienda(tienda_sel))
    datos=repo.datos_tienda(tienda_sel)
    tupla=repo.mes_mayor_facturacion(tienda_sel)
    #st.write(f"Total facturacion {datos[0]["facturacion_total"]}, gastos totales {datos[0]["gastos_totales"]}, mes con mayor facturacion {tupla[1]}")
    col1,col2,col=st.columns(3)
    col1.metric("Total facturacion",datos[0]["facturacion_total"])
    col2.metric("Gastos totales",datos[0]["gastos_totales"])
    col.metric("Ms con mayor facturacion",repo.mes_mayor_facturacion(tienda_sel)[1])
if mes_sel!=None:
    st.table(repo.datos_tabla_mes(mes_sel))