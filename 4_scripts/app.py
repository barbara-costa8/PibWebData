import streamlit as st
import pandas as pd
import sqlalchemy as db
import plotly.express as px
import numpy as np

#engine = db.create_engine('sqlite:///dfpib.db',echo = True)
#conn = engine.connect()

#query = "SELECT * FROM PIB_Países"
#df = pd.read_sql_query(query, engine)

dados = pd.read_csv("0_bases_originais/dados_originais.csv", sep=";", encoding='utf-8')
df = pd.DataFrame(dados)

paises = df['pais'].unique()
regioes = df['regiao'].unique()
anos = df['fmi_ano'].unique()

st.image("https://cdn.borainvestir.b3.com.br/2022/09/01094303/pib-o-que-e-o-produto-interno-bruto.jpeg.webp")  

st.title("Visualização de Dados Econômicos")

regiao_selecionada = st.sidebar.selectbox("Selecione a Região", regioes)
ano_selecionado = st.sidebar.selectbox("Selecione o Ano", anos)

df_filtrado = df[(df['regiao'] == regiao_selecionada) & 
                      (df['fmi_ano'] == ano_selecionado)]

st.subheader(f"Dados da Região: {regiao_selecionada} para o Ano: {ano_selecionado}")

fig_fmi = px.bar(df_filtrado, x='pais', y='fmi_estimativa', title='FMI Estimativa')
st.plotly_chart(fig_fmi)

fig_bm = px.bar(df_filtrado, x='pais', y='bm_estimativa', title='BM Estimativa')
st.plotly_chart(fig_bm)


df_filtrado['diferenca'] = df_filtrado['fmi_estimativa'].str.replace(',', '').astype(float) - df_filtrado['bm_estimativa'].str.replace(',', '').astype(float)
fig_diferenca = px.bar(df_filtrado, x='pais', y='diferenca', title='Diferença FMI e BM')
st.plotly_chart(fig_diferenca)

fig = px.pie(df, 'regiao')
st.plotly_chart(fig)