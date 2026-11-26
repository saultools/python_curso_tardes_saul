from typing import List
from fastapi import FastAPI,APIRouter,HTTPException
from model.libros_model import Libro
from libros_service_05 import LibrosService

router=APIRouter()
service=LibrosService()

@router.post("/libro",response_model=Libro) # POST http://localhost:8000/libro
def guardar_libro(libro:Libro):
    if service.alta_libro(libro)==None:
        raise HTTPException(status_code=409,detail="no se admite isbn repetido")
    return libro
"""json para el POST
{
    "isbn": 458,
    "titulo": "Título",
    "autor": "john Doe",
    "precio": 19.99,
    "paginas": 532,
    "idTema": 2
}
"""

@router.get("/libro/{isbn}",response_model=Libro) # GET http://localhost:8000/libro/458
def buscar_libro(isbn:int):
    return service.buscar_libro(isbn)

@router.delete("/libro/{isbn}") # DELETE http://localhost:8000/libro/458
def eliminar_libro(isbn):
     if service.eliminar_libro(isbn) is False:
         raise HTTPException(status_code=404,detail="libro no encontrado con ese ISBN")
     else: service.eliminar_libro(isbn)