import streamlit as st

saludo = ""
with st.sidebar:
    st.write("Menú navegación")
    st.text_input("dato:")
    if st.button("pulsar"):
        saludo = "estoy en navegación"
st.write(saludo)