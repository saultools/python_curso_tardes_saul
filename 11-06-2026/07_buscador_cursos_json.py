#Ejercicio de Antonio (07, 11-06-2026)
#Realizar una nueva versión del ejercicio 38_buscar_cursos, lo más reducida posible

#Ejercicio de Antonio: (38, 11-04-2026)
# Nombre del curso con la nota más alta
# Nombre del curso que finalizó antes

import datetime as dt
import streamlit as st
import json

jsonfile="07_buscador_cursos.json"
with open(jsonfile,"r",encoding="UTF-8") as f:
    datos=json.load(f)
cursos=datos["cursos"]

def media(numeros):
    if numeros:
        return sum(numeros)/len(numeros)
    else:
        return 0
def convertir_a_fecha(texto):
    return dt.datetime.strptime(texto,"%d/%m/%Y")
def curso_antes():
    curso=min(cursos,key=lambda c:convertir_a_fecha(c["fecha_fin"]))
    
    return f"El curso más antiguo es {curso["denominacion"]}"
    
def curso_media_mayor():
    curso=max(cursos,key=lambda c:media(c["calificaciones"]))
    
    return f"El curso con la media más alta es {curso["denominacion"]}"
    
#llamadas a las funciones
st.write(curso_antes())
st.write(curso_media_mayor()) 

#streamlit run este_filename.py