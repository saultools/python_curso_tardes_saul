from fastapi import FastAPI
import datetime

app=FastAPI()

@app.get("/saludo") # http://127.0.0.1:5000/saludo
def saludar():
    return {"saludo": "Bienvenido a FastAPI",
            "fecha":datetime.date.today()}

@app.get("/saludo/{nombre}") # http://127.0.0.1:5000/saludo/saul
def saludo_personal(nombre):
    return {"saludo": f"Hola {nombre} bienvenido a FastAPI",
            "fecha":datetime.date.today()}

@app.get("/saludo_completo") #http://127.0.0.1:5000/saludo_completo?nombre=saul&edad=55
def saludo_completo(nombre,edad):
    return {"saludo":f"hola {nombre}, tienes {edad} años, bienvenido a FastAPI",
            "fecha":datetime.date.today()}

# la aplicación no se corre desde la consola estándar de python, sino desde "uvicorn 01_saludo:app --reload --port 5000".
# Necesitas instalar con pip: uvicorn y fastapi