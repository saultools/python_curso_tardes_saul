#Ejercicio para casa: con el csv 5: basado en el presuspuesto, dar las casas que se puede permitir el usuario

import csv, streamlit as st

st.title("Buscador de casas")
presupuesto=int(st.number_input(value=0,label="Introduce tu presupuesto: "))

with open("../11-05-2026 - ejercicios_persistencia_datos/105_houses.csv","r") as f:
    row=csv.DictReader(f)
    for casa in row:
        if st.button("Calcular"):
            listadecasas=list(filter(lambda p:float(p["price"])<=presupuesto,csv.DictReader(f)))
            st.table(listadecasas)
    if int(casa["price"]) <= presupuesto:
        st.write(f"casa que entra en tu presuspuesto: {casa}")

#solución de Antonio:
#a partir de un presupuesto, devuelve la lista de 
#casas que se puede permitir
"""
def posibles(presupuesto):
    with open("houses.csv","r") as f:
        todos=list(csv.DictReader(f))
        return [h for h in todos if int(h["price"])<=int(presupuesto)]
pres=st.text_input("Dime tu presupuesto: ")
if st.button("Calcular"):   
    st.table(posibles(pres))
presupuesto = st.number_input("Dime tu presupuesto: ")
with open("houses.csv", "r") as f:
    disponibles=list(filter(lambda p:float(p["price"])<=presupuesto,csv.DictReader(f)))
    st.table(disponibles) 
"""