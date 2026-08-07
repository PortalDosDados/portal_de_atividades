import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(
    page_title="Portal de Atividades", layout="wide", initial_sidebar_state="expanded"
)

# Cabeçalho principal
st.title("Portal de Atividades")
st.markdown("""
    Bem-vindo ao Portal de Atividades. Aqui você encontra exercícios, explicações e material de apoio para estudar metrologia com clareza.
    """)

# Conteúdo da home ensinando a usar a barra lateral
st.subheader("Como navegar pelo portal")
st.markdown("""
    - Abra o menu lateral para ver as opções de exercícios.
    - Selecione um exercício para carregar o conteúdo correspondente.
    - Use os links na lateral para alternar entre os módulos.
    """)

st.info(
    "Importante: a navegação principal está na barra lateral. Se ela estiver recolhida, clique no ícone no canto superior esquerdo."
)

st.write("---")

st.subheader("O que você pode fazer")
st.markdown("""
    1. Verifique a lista de exercícios disponíveis na barra lateral.
    2. Clique no item desejado para abrir a página de cada exercício.
    3. Volte para esta home quando quiser rever o guia de navegação.
    """)

st.write("---")
