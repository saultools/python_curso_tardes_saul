"""
Utilizando los archivos de funciones definidos, hará lo siguiente
1. Borrará las tablas de la base de datos
2. Recuperar continentes y países del JSON
3. Preparará los datos obtenidos, para poder inviarlos a las funciones de la base de datos
4. Llamará a las funciones para guardar los continentes y paises
"""

import operaciones_bd as opbd, operaciones_json as opjs, json

jsonfile = "../11-09-2026/11_countries.json"
with open(jsonfile,"r") as g:
    data = json.load(g)
lista_continentes=set([n["region"] for n in data])
#print(lista_continentes)

opbd.borrar_tablas()

continentes=opjs.continentes() #["Asia","Europe",.]
opbd.crear_continentes(continentes)

continentes_bd=opbd.devolver_continentes() #[{"continente":"Asia",idContinente":3},.]
paises=opjs.paises() #[{"name":"España","region":"Europe"}]

def obtener_idcontinente(continente):
    return [c["idContinente"] for c in continentes_bd if c["continente"]==continente][0]

#formateamos la lista de paises tal y como lo espera la función crear_paises
paises_para_bd=[{"pais":p["name"],
                 "poblacion":p["population"],
                 "bandera":p["flags"]["png"],"idContinente":obtener_idcontinente(p["region"])} for p in paises]
opbd.crear_paises(paises_para_bd)
print("Datos almacenados!!!") 
