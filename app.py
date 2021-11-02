import streamlit as st
import pandas as pd
import numpy as np
import base64
from io import BytesIO
import streamlit as st


# change the app name in browser
st.set_page_config(
    page_title="xapapp",
    page_icon="🧊",
    initial_sidebar_state="expanded")

# initial info
st.title('XAPAPP')
st.write('Aplicació intel·ligent per canviar els preus dels articles.')
st.subheader('Entrada d\'usuari')
uploaded_file = st.file_uploader('Carrega el fitxer XLSX', type=['xlsx'])

# file upload
if uploaded_file is not None:
    st.write('S\'ha pujat un fitxer XLSX.')
    df = pd.read_excel(uploaded_file, sheet_name=None)
    df_mod = df.groupby(['Descripción']).first().reset_index()
    df1 = df_mod[['Descripción','Coste']]
    st.write(df1)
else:
    st.write('S\'està esperant el fitxer XLSX per pujar. Actualment s\'utilitzen paràmetres d\'entrada d\'exemple.')
    df = pd.read_csv('https://raw.githubusercontent.com/dominikapetru/app_mc/main/articles.csv')
    df_mod = df.groupby(['Descripción']).first().reset_index()
    df2 = df_mod[['Descripción','Coste']]
    st.write(df2)

st.subheader('Canvi de preus per familia d\'articles')

# names of the groups of articles
var = df['Descripción'].unique()
desc = var.tolist()


if 'count' not in st.session_state:
    st.session_state.count = 0


# select one group
option1 = st.selectbox('Quina familia de preus vols canviar?', desc)
st.write('Has seleccionat:', option1)
option1 = str(option1)

# select new price
option2 = st.number_input('Quin és el nou preu?')
st.write('Has introduït:', option2)
option2 = float(option2)

# button
if st.button('Confirmar y continuar'):
    mask = (df['Descripción'] == option1)
    df['Coste'][mask] = option2
    st.session_state.count += 1

# final table
st.subheader('Actualització final')
df_mod2 = df.groupby(['Descripción']).first().reset_index()
df3 = df_mod2[['Descripción','Coste']]
st.write(df3, st.session_state.count)


# export to excel
def convert_df(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Sheet1') # <--- here
    writer.save()
    processed_data = output.getvalue()
    return processed_data


xls = convert_df(df)
st.download_button(
    label="Download data as XLSX",
    data=xls,
    file_name='articles.xlsx',
    mime='text/xlsx',
    )