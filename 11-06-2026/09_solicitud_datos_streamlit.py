import streamlit as st
nombre=st.text_input("Introduce tu nombre")
edad=st.number_input("Introduce tu edad")
afiliado=st.checkbox("Afiliado")
curso=st.radio("Elige curso: ",["Python","C++","Java"])
centro=st.selectbox("Elige centro: ",["Leganés","Getafe","Alcobendas","San Blas"])
number = st.number_input("cuantos pasteles", value=110, min_value=55, placeholder="Pedido minimo 55 pasteles.")

if st.button("pulsar"):
    st.success(f"Te llamas {nombre}, tienes {edad} años, y has elegido el curso {curso}")

import streamlit as st
aula = [
{"id": 1, "nombre": "Juan", "edad": 25},
{"id": 2, "nombre": "Ana", "edad": 30},
{"id": 3, "nombre": "Pedro", "edad": 22}
]
st.table(aula)