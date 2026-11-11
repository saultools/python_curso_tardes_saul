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

#Solución de Saúl (incompleta)
import streamlit as st, mysql.connector as sql, gestionalumnos as ga

st.title("Gestión de Alumnos")

tab_alta_alumnos, tab_cursos_y_alumnos, tab_busqueda_alumnos = st.tabs([
    "Alta de alumnos",
    "Cursos x Alumnos",
    "Búsqueda de Alumnos"
])

with tab_alta_alumnos:
    dni = st.text_input("DNI")
    nombre = st.text_input("Nombre")
    email = st.text_input("Email")
    curso = st.text_input("Curso")
    nota = st.number_input("Nota", min_value=0, max_value=10)

    if st.button("Guardar Alumno"):
        res = ga.alta_alumno(dni, nombre, email, curso, nota)
        bien = "Guardado correctamente"
        st.success(f"{res} {bien}")

with tab_cursos_y_alumnos:
    # hacer tabla de columnas que imprima variable tabla
    cursos = ""
    st.selectbox('Curso:', [1,2,3])
    st.table(ga.tabla_alumnos())

with tab_busqueda_alumnos:
    alumno=st.text_input("Introduce DNI para ver datos de alumno",key="key1")
    if st.button(label="buscar",key="key2"):
        alumno=ga.buscar_alumnos(dni)
        if alumno==None:
            st.toast("DNI no encontrado")
        else:
            st.write(f"Nombre :**{alumno["nombre"]}**")
            st.write(f"Email :**{alumno["email"]}**")
            st.write(f"Curso :**{alumno["curso"]}**")
            st.write(f"Nota :**{alumno["nota"]}**") 