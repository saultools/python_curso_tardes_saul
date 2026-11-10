import mysql.connector as sql, streamlit as st

def conectar_bd():
    return sql.connect(
        host="localhost",
        user="root",
        password="root",
        port="3306",
        database="universidad"
        )

def alta_alumno():
    cursor = sql.cursor() #Creating a cursor object using the cursor() method
    query = """INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)
    VALUES ('Mac', 'Mohan', 20, 'M', 2000)""" 
    # Preparing SQL query to INSERT a record into the database.
    try:
        cursor.execute(query) # Executing the SQL command
        sql.commit()  # Commit your changes in the database
    except:
        sql.rollback() # Rolling back in case of error
    sql.close()

def tabla_alumnos():
    poop = "poop"

def buscar_alumnos():
    if alumno == alumnos:
        st.print("query de alumno")
    else:
        st.print("DNI no en bbdd")