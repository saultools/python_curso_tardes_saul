# Ejercicio de Antonio: migra el proyecto 35_libreria.py (11-03-2026) a la libería streamlit
"""
Realiza un progrma para la organizacion de una libreria
un libro tiene tres propiedades: titulo, autor y precio.

Cuando se inicie el programa, se va a mostrar un menu:
1-Nuevo libro
2-Mostrar todos
3-Buscar por titulo
4-Libros por precio maximo
5-Salir

1-Se piden los datos del nuevo libro y se guardan
2-Se muestran los titulos de todos los libros
3-Se le pide el titulo y se muestran todos sus datos
4-Se le pide el precio maximo y se muestran los titulos de los libros cuyo precio sea igual o inferior al introducido
Despues de ejecutar cualquiera de las anteriores opciones, se muestra de nuevo el menu.
Asi hasta que elija la opcion 5 que sale del programa
"""

import streamlit as st

if "libros" not in st.session_state:
    libros = []
    st.session_state.libros = libros

libros = [
    {"titulo": "Serie Fundación (5 libros)", "autor": "Isaaac Asimov", "precio": 65.99},
    {"titulo": "La Trilogía del Imperio", "autor": "Larry Niven", "precio": 62.90},
    {"titulo": "El Ascenso de la Civilización", "autor": "Greg Bear", "precio": 58.40},
    {
        "titulo": "El Legado de los Colonos",
        "autor": "Alastair Reynolds",
        "precio": 61.25,
    },
    {"titulo": "Horizontes de la Humanidad", "autor": "C.J. Cherryh", "precio": 57.80},
]

tab_nuevo, tab_todos, tab_buscar, tab_precios = st.tabs(
    ["Nuevo libro", "Mostrar todos", "Buscar por título", "por precio"]
)

with tab_nuevo:
    titulo = st.text_input("introduce título: ")
    autor = st.text_input("introduce autor: ")
    precio = st.number_input("introduce precio: ")
if st.button("Guardar libro"):
    libros.append({"titulo": titulo, "autor": autor, "precio": precio})

with tab_todos:
    st.title("todos los libros")
    st.table(libros)

with tab_buscar:
    titulo = st.text_input("introduce títuloa buscar: ")
if st.button("buscar"):
    libs = list(filter(lambda lib: lib["titulo"].lower() == titulo.lower(), libros))
    if libs:
        st.success(
            f"Titulo: {libs[0]["titulo"]}, Autor: {libs[0]["autor"]}, Precio: {libs[0]["precio"]}"
        )
    else:
        st.error(f"titulo no encontrado")

with tab_precios:
    titulo = st.header("Tabla de libros ordenados por presupuesto")
    presupuesto = st.number_input(
        label="Enter a number", min_value=0, key="presupuesto0"
    )
    st.button("buscar por presupuesto", key="presupuesto1")

    filtrada = []
    for n in libros:
        if n["precio"] <= presupuesto:
            filtrada.append(n)
    st.table(filtrada)

    st.subheader("Todos los libros, de menor a mayor")
    # preciolibros=libros.sort(libros, key=lambda f: f["precio"])
    preciolibros = sorted(libros, key=lambda f: f["precio"])
    st.table(preciolibros)

# mejorado desde el ejercicio 45_libreria del 11-03-2026.
