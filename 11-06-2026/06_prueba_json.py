import datetime as dt
import streamlit as st
import json

#demostración de Antonio de uso de Json:
jsonfile="06_alumnos.json"
with open(jsonfile,"r") as f:
    alumnos=json.load(f)
for a in alumnos:
    print(a["nombre"])
print(20*"-")