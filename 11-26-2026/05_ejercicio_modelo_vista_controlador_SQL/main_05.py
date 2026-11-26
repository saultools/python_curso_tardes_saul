from fastapi import FastAPI
import libros_controller_05

app=FastAPI()
app.include_router(libros_controller_05.router)

# uvicorn main_05:app --reload 
# (con las llamadas API de libros_controller_05)