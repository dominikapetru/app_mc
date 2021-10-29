import streamlit as st
import pandas as pd
import numpy as np

st.header(XAPAPP)
st.write('Aplicació intel·ligent per canviar els preus dels articles.')
st.subheader('Entrada d\'usuari')
uploaded_file = st.file_uploader('Carrega el fitxer CSV', type=['cvs'])

if uploaded_file is not None:
    st.write('S\'ha pujat un fitxer CSV.')
    df1 = pd.read_csv(uploaded_file)
    df_mod = df1.groupby(['Descripción']).first().reset_index()
    df = df_mod[['Descripción', 'Nombre', 'Coste']]
    st.write(df)
else:
    st.write('S\'està esperant el fitxer CSV per pujar. Actualment s\'utilitzen paràmetres d\'entrada d\'exemple.')
    df2 = pd.read_csv('https://raw.githubusercontent.com/dominikapetru/app_mc/main/articles.csv')
    df_mod = df2.groupby(['Descripción']).first().reset_index()
    df = df_mod[['Descripción', 'Nombre', 'Coste']]
    st.write(df)

st.subheader('Canvi de preus per familia d\'articles')

price0_des = df['Descripción'].values[0]
price0 = st.number_input(label: price0_des)


