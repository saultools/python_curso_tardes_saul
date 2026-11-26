"""
API REST para cursos
Un curso se identifica por codigo,nombre,tematica y precio
Expondrá los siguientes recursos:

-Alta de curso. Se recibe un curso y lo da de alta
Devuelve el curso curso añadido
-Buscar cursos por tematica. Se recibe una temática
y devuelve todos los cursos de esa temática
-Eliminar curso. Se recibe un código de curso, y se elimina
Si el código no es válido(<0) se genera error 409 
"""
from typing import List
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

class Curso(BaseModel):
    codigo:int
    nombre:str
    tematica:str
    precio:float
    
app=FastAPI()
lista_cursos=[]
@app.post("/curso",response_model=Curso)
def alta_curso(curso:Curso):
    lista_cursos.append(curso)
    return curso
@app.get("/cursos",response_model=List[Curso])
def cursos_tematica(tematica:str):
    return [c for c in lista_cursos if c.tematica==tematica]
@app.delete("/curso")
def eliminar_curso(codigo:int):
    if codigo<=0:
        raise HTTPException(status_code=409,detail="Código de curso inválido!")
    lista_cursos=[c for c in lista_cursos if c.codigo!=codigo] 