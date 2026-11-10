"""Proyecto gestión de alumnos:
1. Alta de alumnos: A través de una ventana, se solicitan los datos de un
nuevo alumno y se guardan en la base de datos. No se admiten dnis duplicados
si se proporciona un dni que ya existe, el alumno no se añade
y se avisa mediante un mensaje al usuario

2. Busqueda de alumnos por curso. Se selecciona un curso en un combo
y debajo se muestra una tabla con los datos de todos los alumnos
de ese curso. En cada fila, aparecerá un botón para borrar a ese alumno

3. Busqueda de alumno por dni. Se introduce el dni de un alumno
y se muestran todos sus datos, si no existe, mensaje de advertencia.

Usar streamlit."""

import streamlit as st, mysql.connector as sql, gestionalumnos as ga


st.title("Gestión de Alumnos")

tab_alta_alumnos, tab_cursos_y_alumnos, tab_busqueda_alumnos = st.tabs(
    "Tiendas",
    "Cursos x Alumnos",
    "Búsqueda de Alumnos",
)

with tab_alta_alumnos:
    st.write("a")

with tab_cursos_y_alumnos:
    st.write("a")

with tab_busqueda_alumnos:
    st.write("a")

    alumno=st.text_input("Busca el alumno",key="alumno")
    st.button(label="buscar",key="alumno")