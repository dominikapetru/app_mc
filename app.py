import streamlit as st
import pandas as pd
import numpy as np

st.title('XAPAPP')
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
    df = df_mod[['Descripción','Coste']]
    st.write(df)

st.subheader('Canvi de preus per familia d\'articles')

# names of the groups of articles
var = df['Descripción'].unique()
desc = var.tolist()

# select one group
option1 = st.selectbox(
    'Quina familia de preus vols canviar?',
    desc)
st.write('Has seleccionat:', option1)

# select one group
option2 = st.number_input(
    'Quin és el nou preu?')
st.write('Has introduït:', option2)

# change the group
if option1 and option2 is not None:
    df_new = df[df['Descripción'] == 'option1']
    df_new = df_new.assign(Coste=option2)

else:
    df_new = df

st.write('Actualització final')
df3 = df_new.groupby(['Descripción']).first().reset_index()
df_final = df3[['Descripción','Coste']]
st.write(df_final)


@st.cache
def convert_df(df_final):
    return df_final.to_csv().encode('utf-8')


csv = convert_df(df_final)
st.download_button(
    label="Baixa les dades com a CSV",
    data=csv,
    file_name='articles.csv',
    mime='text/csv',
    )
