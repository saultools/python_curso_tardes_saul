"""Desarrollo API REST alumnos (con Streamlit)
1. Alta de alumno: Recibe los datos de un alumno y lo añade a la base de datos. El mismo email no puede aparecer dos veces en mismo curso. 
Devuelve el alumno añadido. Si no se pudo añadir error con codigo de estado 409.

2. Listado de alumnos. Devuelve todos los alumnos.
3. Alumnos por curso. A partir de un nombre de curso, devuelve todos los alumnos matriculados.
4. Eliminar por email. Elimina el alumno con dicho email. Devuelve el alumno eliminado.

Aclaración: El idAlumno no se proporciona al dar de alta un alumno. Se genera automáticamente.
"""
