# Módulo gestionalumnos para la Solución de Saúl a 15_gestor_alumnos (incompleta)

import mysql.connector as sql, streamlit as st

def conectar_bd():
    return sql.connect(
        host="localhost",
        user="root",
        password="root",
        port="3306",
        database="universidad"
        )

def alta_alumno(dni, nombre, email, curso, nota):
    db=conectar_bd()
    cursor = db.cursor()
    resultado = []
    try:
        query = "INSERT INTO universidad.alumnos (dni, nombre, email, curso, nota) VALUES (%s, %s, %s, %s, %s);"
        valores = (dni, nombre, email, curso, nota)
        cursor.execute(query,valores)
        resultado = cursor.fetchall()
        mensaje = "Alumno insertado correctamente"
    except Exception as e:
        db.rollback()
        mensaje = f"Error al insertar: {e}"
    finally:
        db.close()
    return resultado

def tabla_alumnos():
    db=conectar_bd()
    cursor = db.cursor()
    resultado = []
    try:
        query = "SELECT * FROM universidad.alumnos;"
        cursor.execute(query)
        resultado = cursor.fetchall()
        db.commit()
    except Exception as e:
        print(f"Error: {e}")
        db.rollback()
    finally:
        db.close()
    return resultado

def buscar_alumnos(dni):
    db=conectar_bd()
    cursor = db.cursor(dictionary = True)
    resultado = None
    try:
        query="SELECT * FROM alumnos WHERE dni = %s"
        cursor.execute(query,(dni))
        resultado = cursor.fetchone()
    except Exception as e:
            db.rollback()
            mensaje = f"Error al insertar: {e}"
    finally:
        db.close()
    return resultado

def eliminar_alumno(dni):
    db=conectar_bd()
    cursor=db.cursor(dictionary=True)
    query = "SELECT * from alumnos where dni=%s"
    cursor.execute(query,(dni,))
    resultado = cursor.fetchone() #devuelve el alumno con ese DNI y si no existe, devuelve "NONE"
    db.commit()
    db.close()
    return resultado

"""
def funcion_en_blanco()
    db=conectar_bd()
    cursor = db.cursor()
    resultado = ""
    try:
        query = ""
        cursor.execute(query) # Executing the SQL command
        db.commit()  # Commit your changes in the database
    except:
        db.rollback() # Rolling back in case of error
    db.close()
"""