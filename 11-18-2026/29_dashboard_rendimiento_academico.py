"""Recrear el dashboard de la foto en esta carpeta con streamlit y mathplotlib 
(cortado en la parte de abajo de la foto)
usando información de alumnos.csv y notas.csv. 
Separar las funciones en su propio archivo e importar como módulo.
"""
import streamlit as st, fda

st.set_page_config(layout="wide",page_title="Dashboard Saúl")

id_alumno,nombre,edad,curso,grupo = "","","","",""
id_nota,id_alumno,asignatura,evaluacion,nota = "","","","",""
with st.sidebar:
    st.header("Filtros")
    curso=st.selectbox("Curso",["Todos"]+fda.general_filtrado("curso"),index=None,key=1)
    asignatura=st.selectbox("Asignatura",["Todos"]+fda.general_filtrado("asignatura"),index=None,key=2)
    grupo=st.selectbox("Grupo",["Todos"]+fda.general_filtrado("grupo"),index=None,key=3)
    evaluacion=st.selectbox("Evaluación",["Todos"]+fda.general_filtrado("evaluacion"),index=None,key=4)
    st.write(fda.filtrar_datos().schema)


st.markdown("# 📊 Dashboard de rendimiento académico")

columnas = st.columns([2,2,2,2,2])
columnas[0].metric(label="Alumnos evaluados", value="273 K")
columnas[1].metric(label="Nota media", value="273 K")
columnas[2].metric(label="Nota máxima", value="273 K")
columnas[3].metric(label="Nota mínima", value="273 K")
columnas[4].metric(label="Aprobados", value="273 K")

st.markdown("### Estadísticas por asignatura")
st.dataframe(fda.estadisticas_asignatura(curso, asignatura, grupo, evaluacion),height="content")

st.markdown("### Rendimiento por alumno")
st.dataframe(fda.rendimiento_alumno(curso, asignatura, grupo, evaluacion),height="content")

st.html("<hr>")
st.markdown("### Representación gráfica")

tab1,tab2,tab3 = st.tabs(["Notas por asignatura",
                          "Evolución de Evaluaciones",
                          "Distribución de Notas"])
with tab1:
    with st.container(horizontal_alignment="center",border=True,gap="xlarge"):
        st.pyplot(fda.snap_ventas(), width=600)

with tab2:
    with st.container(horizontal_alignment="center",border=True,gap="xlarge"):
        st.pyplot(fda.snap_ventas(), width=600)

with tab3:
    with st.container(horizontal_alignment="center",border=True,gap="xlarge"):
        st.pyplot(fda.snap_ventas(), width=600)