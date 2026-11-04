# se pide al usuario que introduzca horario y le mostraremos los nombres de los cursos de ese horario

cursos=[
    {"denominacion":"Python y datos","horario":"mañana","fecha_fin":"10/03/2026"},
    {"denominacion":"Inglés científico","horario":"mañana","fecha_fin":"22/07/2026"},
    {"denominacion":"Spring e hibernate","horario":"tarde","fecha_fin":"04/12/2025"},
    {"denominacion":"Programador cerficado","horario":"festivos","fecha_fin":"30/09/2025"}  
] 

#intento de Saúl:
turno_pref=input("introduce tu curso (mañana/tarde/festivos): ")
"""
def horario():
    return
for n in cursos:
    if n["horario"] == turno_pref:
        print(cursos(map(lambda n:n[turno_pref],horario)))
"""
        
#solución de Antonio:
print(list(map(lambda l:l["denominacion"],
               filter(lambda c:c["horario"]==turno_pref,cursos)))) 