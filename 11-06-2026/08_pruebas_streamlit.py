import streamlit as st
import time 
st.success("todo correcto")
mensaje_error=st.error("no ha ido bien, 3 segundos")
time.sleep(3)
mensaje_error.empty()
#st.error("no ha ido bien")
st.toast(f"mensaje flotante",duration="long")