import mysql.connector as con
def crear_conexion():
    return con.connect(host="localhost",
               user="root",
               password="root",
               port=3306,
               database="universidad")
    
def buscar_alumno(dni):
    sql="select * from alumnos where dni=%s"
    db=crear_conexion()
    cursor=db.cursor(dictionary=True)
    cursor.execute(sql,(dni,))
    resultado= cursor.fetchone() #Devuelve el alumno con ese dni. Si no existe devuelve None
    db.close()
    return resultado
def buscar_alumnos_curso(curso):
    sql="select * from alumnos where curso=%s"
    db=crear_conexion()
    cursor=db.cursor(dictionary=True)
    cursor.execute(sql,(curso,))
    resultado=cursor.fetchall()
    db.close()
    return resultado
def alta_alumno(dni,nombre,email,curso,nota):
    sql="insert alumnos(dni,nombre,email,curso,nota) values(%s,%s,%s,%s,%s)"
    db=crear_conexion()
    cursor=db.cursor()
    cursor.execute(sql,(dni,nombre,email,curso,nota))
    db.commit()
    db.close()
def eliminar_alumno(dni):
    sql="delete from alumnos where dni=%s"
    db=crear_conexion()
    cursor=db.cursor()
    cursor.execute(sql,(dni,))  
    db.commit()
    db.close()  
def cursos():
    sql="select distinct(curso) from alumnos"
    db=crear_conexion()
    cursor=db.cursor(dictionary=True)
    cursor.execute(sql)
    resultado=cursor.fetchall() #[{"curso":"Python","curso":"Java"}]
    resultado=[c["curso"] for c in resultado]
    db.close()
    return resultado    
def actualizar(dni,nombre,email,curso,nota):
    sql="update alumnos set nombre=%s, email=%s, curso=%s, nota=%s where dni=%s"
    db=crear_conexion()
    cursor=db.cursor()
    cursor.execute(sql,(nombre,email,curso,nota,dni))
    db.commit()
    db.close() 


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

import streamlit as st
import operaciones_bd as opbd
tab_nuevo_alumno,tab_alumnos_cursos, tab_buscar_alumno=st.tabs(["Nuevo alumno","Buscar por curso","Buscar por DNI"])

    
with tab_nuevo_alumno:
    dni=st.text_input("DNI del alumno: ")
    nombre=st.text_input("Nombre del alumno: ",key="nombre")
    email=st.text_input("Email del alumno: ")
    curso=st.text_input("Curso del alumno: ")
    nota=st.text_input("Nota del alumno: ")
    if st.button("Alta alumno"):
        if opbd.buscar_alumno(dni)==None:
            opbd.alta_alumno(dni,nombre,email,curso,nota)
        else:
            st.toast("El dni ya existe!!")
with tab_alumnos_cursos:
    curso=st.selectbox("Selecciona curso",opbd.cursos())
    if curso:
        col_nombre,col_email,col_dni,col_nota,col_eliminar=st.columns([2,3,1,1,2])
        alumnos=opbd.buscar_alumnos_curso(curso)
        for a in alumnos:
            col_nombre.write(a["nombre"])
            col_email.write(a["email"])
            col_dni.write(a["dni"])
            col_nota.write(a["nota"])
            if col_eliminar.button("Eliminar",key=f"eliminar{a["dni"]}"):
                opbd.eliminar_alumno(a["dni"])
                st.rerun()
with tab_buscar_alumno:
    dni=st.text_input("Introduce el DNI: ")
    if st.button("Buscar alumno") or dni:
        alumno=opbd.buscar_alumno(dni)
        if alumno==None:
            st.toast("El dni no existe!!")
        else:
            nombre=st.text_input("Nombre :",value=alumno["nombre"])
            email=st.text_input("Email :",value=alumno["email"])
            curso=st.text_input("Curso :",value=alumno["curso"])
            nota=st.text_input("Nota :",value=alumno["nota"])
            if st.button("Actualizar"):
                opbd.actualizar(dni,nombre,email,curso,nota)
                