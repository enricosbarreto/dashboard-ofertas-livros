"""Dashboard de Livros: app Streamlit.
"""

import streamlit as st
from dados import processar_dados

st.title("📚 Dashboard de Livros")

livros, preco_medio, contagem_5_estrelas = processar_dados()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Total de Livros", value=len(livros))

with col2:
    st.metric(label="Preço Médio", value=f"R$ {preco_medio:.2f}")

with col3:
    st.metric(label="Livros 5 Estrelas", value=contagem_5_estrelas)

st.subheader("Lista de Ofertas")
st.dataframe(livros)