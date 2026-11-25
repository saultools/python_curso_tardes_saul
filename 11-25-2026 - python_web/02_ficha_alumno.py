# Hacer un API rest con una función:
# que reciba un DNI de el alumno y devuelva su ficha (objeto Json), formada por: dni,nombre,edad y email.

from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel

"""class Alumno:
    def __init__(self,dni,nombre,edad,email):
        self.dni=dni
        self.nombre=nombre
        self.edad=edad
        self.email=email"""
class Alumno(BaseModel):
    dni:str
    nombre:str
    edad:int
    email:str

app=FastAPI()

@app.get("/ficha/{dni}",response_model=Alumno) # GET http://localhost:5000/ficha/12345678A
def ficha(dni):
    if dni==None:
        return None
    return Alumno(dni=dni,nombre="prueba",edad=20,email="prueba@gmail.com")
    
@app.post("/ficha",response_model=Alumno) # POST http://localhost:5000/ficha
def nueva_ficha(ficha:Alumno):
    if len(ficha.dni)<2:
        raise HTTPException(status_code=418,detail="No es posible dar de alta sin DNI Válido")
    print(ficha.nombre)
    return ficha 

@app.delete("/ficha/{dni}",response_model=Alumno) # DELETE http://localhost:5000/ficha/12345678A
def eliminar_ficha(dni,res:Response):
    print("eliminando DNI {dni}")

# comando: uvicorn 02_ficha_alumno:app --reload --port 5000