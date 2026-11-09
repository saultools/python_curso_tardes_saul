""" Usando streamlit y 11_countries.json, crea una página de una pestaña que cargue 
todos los datos del Json (usando una tabla de columnas), 
y una función de filtrado por continente (filtra por búsqueda escrita). """

# solución de Saúl (incompleta, pero no necesariamente mal)
import streamlit as st,json

jsonfile="11_countries.json"
with open(jsonfile,"r") as f:
    countries=json.load(f)

def paises_continente(continente):
    with open(jsonfile,"r") as f:
        return list(filter(lambda p:p["region"]==continente,json.load(f)))
def continentes():
    with open(jsonfile,"r") as f:
        return list(set(map(lambda p:p["region"],json.load(f))))

tab_continents, tab_2, tab_3 = st.tabs(["Búsqueda por continente","pestaña B","Solución de Antonio"])

with tab_continents:
    left, middle, right = st.columns(3, vertical_alignment="bottom")
    left.text_input("Write something")
    middle.button("Click me", width="stretch")
    right.checkbox("Check me")
    
with tab_2:
    st.title("Más contenido próximamente")
    st.table(countries)

# solución de Antonio (en tab 3):
with tab_3:
    import streamlit as st,json
    
    def paises_continente(continente):
        with open(jsonfile,"r") as f:
            return list(filter(lambda p:p["region"]==continente,json.load(f)))
    def continentes():
        with open(jsonfile,"r") as f:
            return list(set(map(lambda p:p["region"],json.load(f))))

    continente= st.selectbox("**Seleccione continente:**",continentes())
    
    if continente:
        paises=paises_continente(continente)
        col_pais,col_continente,col_poblacion,col_bandera=st.columns(4)
        col_pais.write("**Pais**")
        col_continente.write("**Continente**")
        col_poblacion.write("**Población**")
        col_bandera.write("**Bandera**")
        
        for pais in paises:
            col_pais,col_continente,col_poblacion,col_bandera=st.columns(4)
            col_pais.write(pais["name"])
            col_continente.write(pais["region"])
            col_poblacion.write(pais["population"])
            col_bandera.image(pais["flags"]["png"],width=50) 