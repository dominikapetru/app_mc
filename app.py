import streamlit as st
import pandas as pd
import numpy as np
import base64
from io import BytesIO

st.title('XAPAPP')
st.write('Aplicació intel·ligent per canviar els preus dels articles.')
st.subheader('Entrada d\'usuari')
uploaded_file = st.file_uploader('Carrega el fitxer XLSX', type=['xlsx'])

if uploaded_file is not None:
    st.write('S\'ha pujat un fitxer XLSX.')
    df1 = pd.read_excel(uploaded_file)
    df_mod = df1.groupby(['Descripción']).first().reset_index()
    df = df_mod[['Descripción', 'Nombre', 'Coste']]
    st.write(df)
else:
    st.write('S\'està esperant el fitxer XLSX per pujar. Actualment s\'utilitzen paràmetres d\'entrada d\'exemple.')
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


st.subheader('Actualització final')

# change the value of price
df_final = df.loc[df.Descripción == option1, "Coste"] = option2
st.write(df_final)


def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1')
    writer.save()
    processed_data = output.getvalue()
    return processed_data


def get_table_download_link(df):
    val = to_excel(df)
    b64 = base64.b64encode(val)
    return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="extract.xlsx">Download csv file</a>'


# collect data and export file
df = df_final
st.markdown(get_table_download_link(df), unsafe_allow_html=True)
