#trabajando con Diccionarios: Demostración de Antonio
ciudades={}
ciudades["Madrid"]=2300000
ciudades["Getafe"]=100000
ciudades["Alcorcón"]=120000
ciudades["Ávila"]=130000
del(ciudades["Ávila"])

for k,v in ciudades.items():
    print(f"La ciudad {k} tiene {v} habitantes")
