import streamlit as st
import empleados_repository as repo

tab_nuevo,tab_2,tab_filtro=st.tabs(["Nuevo empleado",
                                       "Actualización de datos",
                                       "Búsqueda de empleados"])

with tab_nuevo:
    empleado=st.text_input("Nombre del empleado: ")
    edad=st.number_input("Edad del empleado: ")
    salario=st.number_input("Salario del empleado: ")
    departamento=st.text_input("Departamento del empleado: ")

    if st.button("Alta empleado"):
        repo.nuevo_empleado(empleado,edad,salario,departamento)
        st.toast("Empleado agregado!!")

# Ejercicio 13-11-2026: Muestra la tabla con todos los empleados,
# permitiendo la modificación de sus datos. Mediante un botón "Actualizar",
# se grabarán los cambios. Utilizar data_editor(datos).
with tab_2:
    st.markdown("### Editar empleado")
    resultado=st.data_editor(repo.todos_empleados(),disabled=["_id"])
    if st.button("Actualizar"):
        repo.editar_empleado(resultado)
        st.success("Datos actualizados correctamente")
        st.rerun()

    #st.markdown(" #### Lista de todos los empleados: ")
    #st.dataframe(repo.todos_empleados())

with tab_filtro:
    filtro=st.radio("Tipo de filtro",
                    ["Por departamento", 
                    "Por salarios"])
    
    if filtro=="Por departamento":
        dep=st.selectbox("Seleccione departamento",repo.departamentos())
        st.dataframe(repo.empleados_por_departamento(dep))
    else:
        min=st.number_input("Salario mínimo")
        max=st.number_input("Salario máximo")
        if st.button("Buscar:"):
            st.dataframe(repo.empleados_por_salarios(float(min),float(max)))