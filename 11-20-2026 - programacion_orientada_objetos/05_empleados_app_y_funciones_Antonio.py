#app.py
import empleados_service as ep
import streamlit as st
url="../empleados.csv"
egestor=ep.Gestor_Empleados(url)

tab_nuevo,tab_buscar,tab_departamentos=st.tabs(["Nuevo empleado","Buscar empleado","Empleados por departamento"])

with tab_nuevo:
    st.subheader("Alta de empleados")
    nombre=st.text_input("Nombre:")
    edad=st.number_input("Edad:",value=0)
    salario=st.number_input("Salario:",value=0)
    departamento=st.text_input("Departamento:")
    if st.button("Guardar"):
        empleado=ep.Empleado(nombre,edad,salario,departamento)
        egestor.alta_empleado(empleado)
        st.toast("Empleado añadido!")
    
with tab_buscar:
    st.subheader("Búsqueda de empleado")
    nombre=st.text_input("Nombre:",key="fnombre")
    if st.button("Buscar"):
        empleado=egestor.buscar_empleado(nombre)
        if empleado!=None:
            st.write(f"Nombre: {empleado.nombre}")
            st.write(f"Edad: {empleado.edad}")
            st.write(f"Salario: {empleado.salario}")
            st.write(f"Departamento: {empleado.departamento}")
        else:
            st.toast("Empleado no existente!!")
    
with tab_departamentos:
    st.subheader("Empleados por departamento")
    departamento=st.text_input("Departamento: ",key="dep2")
    if st.button("Buscar empleados"):
        empleados=egestor.empleados_departamento(departamento)
        empleados=[vars(e) for e in empleados]
        st.table(empleados)

# empleados_service.py
import csv
class Empleado:
    def __init__(self,nombre,edad,salario,departamento):
        self.nombre=nombre
        self.edad=edad
        self.salario=salario
        self.departamento=departamento
        
class Gestor_Empleados:
    def __init__(self,dir):
        self.dir=dir
    def alta_empleado(self,empleado):
        with open(self.dir,"a",newline="") as f:
            csv.writer(f).writerow([empleado.nombre,empleado.edad,empleado.salario,empleado.departamento])

    def buscar_empleado(self,nombre):
       with open(self.dir,"r") as f:
            for e in csv.reader(f):
                if e[0]==nombre:
                    return Empleado(e[0],int(e[1]),float(e[2]),e[3])
            return None
    def empleados_departamento(self,departamento):
        with open(self.dir,"r") as f:
            datos=list(csv.DictReader(f))
            return [Empleado(e["empleado"],int(e["edad"]),float(e["salario"]),e["departamento"]) for e in datos if e["departamento"]==departamento]
        