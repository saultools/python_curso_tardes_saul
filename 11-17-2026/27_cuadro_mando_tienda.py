"""*Al seleccionar una tienda se mostrara:
Una tabla con la información de dicha tienda. Y debajo de esa tabla:
-total de facturación
-total de gastos de personal
-mes con mayor facturación

*Al seleccionar un mes se mostrará:
Una tabla con los datos de ese mes. Y debajo de esa tabla:
-Media de facturación de todas las tiendas
-Tienda con mayor gasto de personal """

import tiendas_repository as tr, streamlit as st

tienda,mes = "",""

with st.sidebar:
    st.header("Información por tienda")
    tienda=st.selectbox("Seleccione una tienda",tr.tiendas_ver(),index=None)
    
    st.header("Información por mes")
    mes=st.selectbox("Seleccione una tienda",tr.mes_ver(),index=None)

if tienda is not None:
    st.markdown(f"## {tienda}")
    st.dataframe(tr.tienda_filtrada(tienda))
    st.markdown("### Totales")
elif mes is not None:
    st.markdown(f"## {mes}")
    st.dataframe(tr.mes_filtrado(mes))
    st.markdown("### Totales")
else:
    st.markdown("# Tabla general (todo)")
    st.dataframe(tr.df)

    columnas = st.columns([2, 2, 1])
    columnas[0].write("texto 1")
    columnas[1].write("texto 2")
    columnas[2].markdown(f"<p style='font-size: 1em; font-weight: bold;'>texto</p>",unsafe_allow_html=True)

    st.html("<hr>")
    fotitos = st.columns([2, 3])
    fotitos[0].markdown(f"### Ventas por tienda")
    fotitos[1].pyplot(tr.snap_ventas(),width="content")
