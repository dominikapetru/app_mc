import streamlit as st
import pandas as pd
import numpy as np
import base64
from io import BytesIO
import streamlit as st


# change the app name in browser
st.set_page_config(
    page_title="xapapp",
    page_icon="馃",
    initial_sidebar_state="expanded")

# initial info
st.title('XAPAPP')
st.write('Aplicaci贸 intel路ligent per canviar els preus dels articles.')
st.subheader('Entrada d\'usuari')
uploaded_file = st.file_uploader('Carrega el fitxer XLSX', type=['xlsx'])

# file upload
if uploaded_file is not None:
    st.write('S\'ha pujat un fitxer XLSX. Aquestes s贸n els fam铆lies de materials.')
    df = pd.read_excel(uploaded_file)
    df_mod = df.groupby(['Descripci贸n']).first().reset_index()
    df1 = df_mod[['Descripci贸n','Coste']]
    st.write(df1)
else:
    st.write('S\'est脿 esperant el fitxer XLSX per pujar. Actualment s\'utilitzen par脿metres d\'entrada d\'exemple.')
    df = pd.read_csv('https://raw.githubusercontent.com/dominikapetru/app_mc/main/articles.csv')
    df_mod = df.groupby(['Descripci贸n']).first().reset_index()
    df2 = df_mod[['Descripci贸n','Coste']]
    st.write(df2)

st.subheader('Canvi de preus per familia d\'articles')

# names of the groups of articles
var1 = df['Descripci贸n'].unique()
var2 = np.sort(var1)
desc = var2.tolist()

# list of new prices
prices = []
i = 0

# changing prices for each group
with st.form('my form'):
    for i in range(len(desc)):
        num = i+1
        num = str(num)
        st.write(num, desc[i])
        y = df.loc[df.Descripci贸n == desc[i], "Coste"]
        z = y.iloc[0]
        x = st.number_input('Quin 茅s el nou preu?', key=i, value=z)
        x = float(x)
        prices.append(x)
    submitted = st.form_submit_button(label='Submit')

    if submitted:
        for i in range(len(desc)):
            mask = (df['Descripci贸n'] == desc[i])
            df['Coste'][mask] = prices[i]


# table
st.subheader('Preus actualitzats')
df_mod2 = df.groupby(['Descripci贸n']).first().reset_index()
df3 = df_mod2[['Descripci贸n', 'Coste']]
st.write(df3)


# export to excel
@st.cache
def convert_df(df_to_convert):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Sheet1')
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