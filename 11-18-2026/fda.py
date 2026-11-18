# funciones_dashboard_academico
import matplotlib.pyplot as mpy, polars as pl

alumnoscsv = "./alumnos.csv"
#id_alumno,nombre,edad,curso,grupo
dfa = pl.read_csv(alumnoscsv)

notascsv = "./notas.csv"
#id_nota,id_alumno,asignatura,evaluacion,nota
dfn = pl.read_csv(notascsv)
dfn = dfn.with_columns(pl.col("nota").cast(pl.Float64, strict=False)) # transforma la columna notas a float

dfmix =dfa.join(dfn,on="id_alumno",how="inner") 
# unir dataframes en base a una key común

def general_filtrado(valor): 
    return dfmix[valor].unique().to_list()
#"valor" recibe el string (se lo pasa la llamada a la función)
# el nombre de los valores de la columna del datafame a mostrar en el selectbox
# (curso,asignatura,grupo,evaluacion)


def filtrar_datos(curso=None, asignatura=None, grupo=None, evaluacion=None):
    datos = dfmix
    filtros = {"curso": curso,"asignatura": asignatura,
               "grupo": grupo,"evaluacion": evaluacion,}
    
    for columna, valor in filtros.items():
        if valor is not None and valor != "Todos":
            datos = datos.filter(pl.col(columna) == valor)
    return datos 
# en esta función creamos un dataframe "datos" basado en el estado de los selecbox,
# para pasarselo a los dataframes de estadisicas alumnos y rendimiento por alumno.

# Esta función "intermedia" es necesaria para poder hacer luego cálculos sobre este dataframe "datos"
# ya filtrado.

def estadisticas_asignatura(curso=None, asignatura=None, grupo=None, evaluacion=None):
    datos = filtrar_datos(curso, asignatura, grupo, evaluacion)
    return datos.group_by("asignatura").agg(
        pl.col("id_alumno").unique().len().alias("Alumnos evaluados"),
        pl.col("nota").mean().alias("Nota Media"),
        pl.col("nota").max().alias("Nota máxima"),
        pl.col("nota").sum().alias("Porcentaje de aprobados")
    )   

def rendimiento_alumno(curso=None, asignatura=None, grupo=None, evaluacion=None):
    datos = filtrar_datos(curso, asignatura, grupo, evaluacion)
    return datos

def snap_ventas():
    edificios = ["Oficinas", "Almacén", "Fábrica", "Tienda"]
    consumo = [350, 220, 580, 190]

    fig, ax = mpy.subplots()
    ax.pie(
        consumo,
        labels=edificios,
        autopct="%1.1f%%"
    )
    return fig