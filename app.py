import streamlit as st
import pandas as pd
import numpy as np

st.header("""
# XAPAPP
Aplicació intel·ligent per canviar els preus dels articles.
""")

st.subheader('Entrada d\'usuari')
uploaded_file = st.file_uploader('Carrega el fitxer CSV', type=['xlsx'])


if uploaded_file is not None:
    st.write('S\'ha pujat un fitxer CSV.')
    df = pd.read_csv(uploaded_file)
    df_mod = df.groupby(['Descripción']).first().reset_index()
    d1 = df_mod[['Descripción', 'Nombre', 'Coste']]
    st.write(d1)
else:
    st.write('S\'està esperant el fitxer CSV per pujar. Actualment s\'utilitzen paràmetres d\'entrada d\'exemple.')
    df_example = pd.read_csv('https://raw.githubusercontent.com/dominikapetru/app_mc/main/articles.csv')
    df_mod = df_example.groupby(['Descripción']).first().reset_index()
    d2 = df_mod[['Descripción', 'Nombre', 'Coste']]
    st.write(d2)
