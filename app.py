import pandas as pd
import streamlit as st

st.set_page_config(page_title="Dashboard de vendas", layout="wide")
st.title("📊 Dashboard de vendas")

# Dados de exemplo
dados = pd.DataFrame({
    "Data": pd.date_range("2026-01-01", periods=6),
    "Produto": ["Camiseta", "Calça", "Camiseta", "Calça", "Camiseta", "Calça"],
    "Valor": [100, 200, 150, 300, 120, 250],
})

# Filtro na barra lateral
produto = st.sidebar.selectbox(
    "Selecione o produto",
    ["Todos", "Camiseta", "Calça"],
)

filtrados = dados
if produto != "Todos":
    filtrados = dados[dados["Produto"] == produto]

# Indicadores
coluna1, coluna2 = st.columns(2)

total = filtrados["Valor"].sum()
coluna1.metric("Faturamento", f"R$ {total}")
coluna2.metric("Quantidade de vendas", len(filtrados))

# Gráfico
st.subheader("Vendas por dia")
vendas_por_dia = filtrados.groupby("Data")["Valor"].sum()
st.line_chart(vendas_por_dia)

# Tabela
st.subheader("Detalhamento")
st.dataframe(filtrados, hide_index=True)