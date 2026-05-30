import streamlit as st
import pandas as pd

from consultas import dados

# dataframe
df = pd.DataFrame(dados)

# título
st.title("Dashboard de Vendedores")

# tabela
st.dataframe(df)

# gráfico
st.bar_chart(
    data=df,
    x="NOME",
    y="NUMERO_NOTAS"
)


# Abra o terminal e rode: streamlit run app.py