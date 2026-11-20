""""Aplicación empleados.
-Alta de nuevo empleados
-Busqueda de empleados por departamento
-Busqueda de un empleado a partir de su nombre"""

import empleados_service_05 as ep,streamlit as st, pandas as pd
filepath="../11-12-2026/empleados.csv"
egestor=ep.Gestor_Empleados(filepath)

tab_nuevo,tab_buscar,tab_departamentos=st.tabs(["Nuevo empleado",
                                              "Buscar empleado",
                                              "Buscar por Departamento"])

with tab_nuevo:
    nombre = st.text_input("nombre")
    edad = st.number_input("edad, en años",value=0)
    salario = st.number_input("salario mensual")
    departamento = st.selectbox("Departamento",ep.general_filtrado("[departamento]"),index=None,key=1)
    if st.button("guardar"):
        nuevo = ep.Empleado(nombre,edad,salario,departamento)
        egestor.alta_empleado(nuevo)
        st.toast("guardado")

with tab_buscar:
    # st.markdown("# Búsqueda de empleado")
    nombre=st.text_input("Nombre:",key="fnombre")
    if st.button("Buscar"):
        empleado=egestor.buscar_empleado(nombre.lower())
        if empleado!=None:
            st.write(f"Nombre: {empleado.nombre}")
            st.write(f"Edad: {empleado.edad}")
            st.write(f"Salario: {empleado.salario}")
            st.write(f"Departamento: {empleado.departamento}")
        else:
            st.toast("Empleado no existente!!")

with tab_departamentos:
    st.markdown("### Búsqueda por departamento")
    departamento = st.selectbox("Departamento",ep.general_filtrado("[departamento]"),index=None,key=2)
    st.table(egestor.empleados_departamento(departamento))

    # st.markdown("### Todos los empleados")
    # tabla_entera = pd.read_csv(filepath)
    # st.table(tabla_entera)