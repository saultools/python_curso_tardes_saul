# En el ejercicio 38 recorremos los cursos y guardamos el resultado mejor.
if False:
    def media(numeros):
        suma=0
        for n in numeros:
            suma+=n
        return suma/len(numeros)

    # Buscamos el curso con la media más alta.
    def curso_media_mayor():
        nombre_curso=cursos[0]["denominacion"]
        media_alta=media(cursos[0]["calificaciones"])
        for c in cursos:
            m=media(c["calificaciones"])
            if m>media_alta:
                media_alta=m
                nombre_curso=c["denominacion"]
        return nombre_curso

    # Convertimos las fechas para poder compararlas.
    def convertir_a_fecha(texto):
        return dt.datetime.strptime(texto,"%d/%m/%Y")

    # Buscamos el curso que termina antes.
    def curso_antes():
        nombre_curso=cursos[0]["denominacion"]
        fecha_antes=convertir_a_fecha(cursos[0]["fecha_fin"])
        for c in cursos:
            f=convertir_a_fecha(c["fecha_fin"])
            if f<fecha_antes:
                fecha_antes=f
                nombre_curso=c["denominacion"]
        return nombre_curso

    # Con max y min no hace falta escribir los bucles.
    # key indica qué dato comparamos de cada curso.
    curso_media=max(cursos,key=lambda c:sum(c["calificaciones"])/len(c["calificaciones"]))
    curso_antes=min(cursos,key=lambda c:convertir_a_fecha(c["fecha_fin"]))

