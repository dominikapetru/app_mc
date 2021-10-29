import streamlit as st
import pandas as pd
import numpy as np

st.write("""
# XAPAPP
Aplicació intel·ligent per canviar els preus dels articles.
""")

st.subheader('Entrada d\'usuari')
uploaded_file = st.file_uploader('Carrega el fitxer CSV', type=['xlsx'])

if uploaded_file is not None:
    st.write('S\'ha pujat un fitxer CSV.')
    df = pd.read_csv(uploaded_file)
    df = df[:5]
    st.write(df)
else:
    st.write('S\'està esperant el fitxer CSV per pujar. Actualment s\'utilitzen paràmetres d\'entrada d\'exemple.')
    df_example = pd.read_csv('https://raw.githubusercontent.com/dominikapetru/app_mc/main/articles.csv')
    df_example = df_example[:5]
    st.write(df_example)
