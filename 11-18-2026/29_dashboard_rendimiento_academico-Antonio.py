"""Recrear el dashboard de la foto en esta carpeta con streamlit y mathplotlib 
(cortado en la parte de abajo de la foto)
usando información de alumnos.csv y notas.csv. 
Separar las funciones en su propio archivo e importar como módulo.
solución de Antonio:"""

#formacion_repository.py
import polars as pl
import streamlit as st


def cargar_datos():

    alumnos = pl.read_csv("alumnos.csv")
    notas = pl.read_csv("notas.csv")

    datos = notas.join(
        alumnos,
        on="id_alumno",
        how="inner"
    )

    return datos


def obtener_cursos():

    datos = cargar_datos()

    return sorted(datos["curso"].unique().to_list())


def obtener_asignaturas():

    datos = cargar_datos()

    return sorted(datos["asignatura"].unique().to_list())


def obtener_grupos():

    datos = cargar_datos()

    return sorted(datos["grupo"].unique().to_list())


def obtener_evaluaciones():

    datos = cargar_datos()

    return sorted(datos["evaluacion"].unique().to_list())
#a partir de los filtros recibidos, filtramos el dataframe global
#eta función será llamada por las demás
def obtener_datos_filtrados(curso, asignatura, evaluacion, grupo):

    resultado =  cargar_datos()

    if curso != "Todos":
        resultado = resultado.filter(
            pl.col("curso") == curso
        )

    if asignatura != "Todas":
        resultado = resultado.filter(
            pl.col("asignatura") == asignatura
        )

    if evaluacion != "Todas":
        resultado = resultado.filter(
            pl.col("evaluacion") == evaluacion
        )

    if grupo != "Todos":
        resultado = resultado.filter(
            pl.col("grupo") == grupo
        )

    return resultado

def obtener_indicadores(curso, asignatura, evaluacion, grupo):

    datos = obtener_datos_filtrados(curso, asignatura, evaluacion, grupo)

    indicadores = datos.select(
        pl.col("id_alumno").unique().count().alias("alumnos"),
        pl.col("nota").mean().alias("media"),
        pl.col("nota").max().alias("maxima"),
        pl.col("nota").min().alias("minima"),
        (
            (pl.col("nota") >= 5).mean() * 100
        ).alias("porcentaje_aprobados")
    )
    return indicadores.row(0,named=True) ##devuelve los indicadores en un diccionario
def obtener_estadisticas_asignaturas(curso, asignatura, evaluacion, grupo):
    datos = obtener_datos_filtrados(curso, asignatura, evaluacion, grupo)
    resultado = datos.group_by("asignatura").agg(
        pl.col("id_alumno").unique().count().alias("alumnos_evaluados"),

        pl.col("nota").mean().round(2).alias("nota_media"),

        pl.col("nota").max().alias("nota_maxima"),

        ((pl.col("nota") >= 5).mean() * 100).round(2).alias("porcentaje_aprobados")
    )

    return resultado.sort("nota_media",descending=True)

def obtener_estadisticas_alumnos(curso, asignatura, evaluacion, grupo):
    datos = obtener_datos_filtrados(curso, asignatura, evaluacion, grupo)
    print(datos)
    por_asignatura = datos.group_by(["id_alumno", "nombre", "curso", "grupo", "asignatura"]).agg(
        pl.col("nota").mean().alias("media_asignatura")
    )
    resultado = por_asignatura.group_by(["id_alumno", "nombre", "curso", "grupo"]).agg(
        pl.col("media_asignatura").mean().round(2).alias("nota_media"),

        pl.col("media_asignatura").count().alias("asignaturas_evaluadas"),

        ((pl.col("media_asignatura") >= 5).sum()).alias("asignaturas_aprobadas")
    )

    return resultado.sort(
        "nota_media",
        descending=True
    )

def obtener_evolucion_evaluaciones(curso, asignatura, grupo):
    resultado = cargar_datos()

    if curso != "Todos":
        resultado = resultado.filter(pl.col("curso") == curso)

    if asignatura != "Todas":
        resultado = resultado.filter(pl.col("asignatura") == asignatura)

    if grupo != "Todos":
        resultado = resultado.filter(pl.col("grupo") == grupo)

    return resultado.group_by("evaluacion").agg(
            pl.col("nota").mean().round(2).alias("nota_media")
        ).sort("evaluacion")

#app.py
import streamlit as st
import matplotlib.pyplot as plt

import formacion_repository as repo


st.set_page_config(
    page_title="Análisis académico",
    layout="wide"
)
#####################
##Funciones para gráficos#######
def grafico_notas_asignaturas(datos): #Recibe dataframe
    fig,gr=plt.subplots()
    gr.bar(
        datos["asignatura"].to_list(),
        datos["nota_media"].to_list()
    )

    gr.set_title("Nota media por asignatura")
    gr.set_xlabel("Asignatura")
    gr.set_ylabel("Nota media")
    gr.set_ylim(0,10)
    return fig

def grafico_evolucion_evaluaciones(datos):
    fig,gr=plt.subplots()
    gr.plot(
        datos["evaluacion"].to_list(),
        datos["nota_media"].to_list(),
        marker="o"
    )

    gr.set_title("Evolución de las notas")
    gr.set_xlabel("Evaluación")
    gr.set_ylabel("Nota media")

    gr.set_xticks(datos["evaluacion"].to_list())
    gr.set_ylim(0, 10)

    plt.grid(alpha=0.3)
    return fig

def grafico_distribucion_notas(datos):
    fig, gr = plt.subplots()
    gr.hist(
        datos["nota"].to_list(),
        bins=10,
        range=(0, 10),
        edgecolor="black"
    )

    gr.set_title("Distribución de calificaciones")
    gr.set_xlabel("Nota")
    gr.set_ylabel("Número de calificaciones")

    gr.set_xticks(range(0, 11))
    return fig



#########################




st.sidebar.title("Filtros")

curso = st.sidebar.selectbox("Curso",["Todos"] + repo.obtener_cursos())

asignatura = st.sidebar.selectbox("Asignatura",["Todas"] + repo.obtener_asignaturas())

grupo = st.sidebar.selectbox("Grupo",["Todos"] + repo.obtener_grupos())

evaluacion = st.sidebar.selectbox("Evaluación",["Todas"] + repo.obtener_evaluaciones())

#Dashboard
st.title("Dashboard de rendimiento académico")
#indicadores
indicadores = repo.obtener_indicadores(
    curso,
    asignatura,
    evaluacion,
    grupo
)

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(
    "Alumnos evaluados",
    indicadores["alumnos"]
)

col2.metric(
    "Nota media",
    f"{indicadores['media']:.2f}"
)

col3.metric(
    "Nota máxima",
    f"{indicadores['maxima']:.2f}"
)

col4.metric(
    "Nota mínima",
    f"{indicadores['minima']:.2f}"
)

col5.metric(
    "Aprobados",
    f"{indicadores['porcentaje_aprobados']:.1f}%"
)

#estadísticas por asignatura
st.subheader("Estadísticas por asignatura")

estadisticas_asignaturas = repo.obtener_estadisticas_asignaturas(
    curso,
    asignatura,
    evaluacion,
    grupo
)

st.dataframe(estadisticas_asignaturas)

#estadísticas por alumno
st.subheader("Rendimiento por alumno")

estadisticas_alumnos = repo.obtener_estadisticas_alumnos(
    curso,
    asignatura,
    evaluacion,
    grupo
)

st.dataframe(estadisticas_alumnos)


#graficos
st.subheader("Representación gráfica")

tab1, tab2, tab3 = st.tabs([
    "Notas por asignatura",
    "Evolución de evaluaciones",
    "Distribución de notas"
])
with tab1:
    fig=grafico_notas_asignaturas(estadisticas_asignaturas)
    st.pyplot(fig)
    plt.close(fig)
    

with tab2:
    evolucion=repo.obtener_evolucion_evaluaciones(curso,asignatura,grupo)
    fig=grafico_evolucion_evaluaciones(evolucion)
    st.pyplot(fig)
    plt.close(fig)

with tab3:

    fig = grafico_distribucion_notas(repo.obtener_datos_filtrados(curso,asignatura,evaluacion,grupo)) #función que devuelve todos los datos filtrados

    st.pyplot(fig)
    plt.close(fig)