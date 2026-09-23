"""Dashboard de Livros: app Streamlit.
"""

import streamlit as st
from dados import processar_dados

st.title("📚 Dashboard de Livros")

livros, preco_medio, contagem_5_estrelas, livro_mais_caro = processar_dados()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="Total de Livros", value=len(livros))

with col2:
    st.metric(label="Preço Médio", value=f"£ {preco_medio:.2f}")

with col3:
    st.metric(label="Livros 5 Estrelas", value=contagem_5_estrelas)

with col4:
    if livro_mais_caro:
        preco_mais_caro = livro_mais_caro.get('preco', '')
        titulo_mais_caro = livro_mais_caro.get('titulo', '')
        st.metric(label="Mais Caro", value=f"{preco_mais_caro}", delta=titulo_mais_caro, delta_color="normal")

st.subheader("Lista de Ofertas")
st.dataframe(livros)