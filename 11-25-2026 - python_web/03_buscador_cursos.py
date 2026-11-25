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

