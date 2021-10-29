import streamlit as st
import pandas as pd
import numpy as np

st.write("""
# XAPAPP
Aplicació intel·ligent per canviar els preus dels articles.
""")

st.subheader('Entrada d\'usuari')
uploaded_file = st.file_uploader("Carrega el fitxer CSV", type=["csv"])



