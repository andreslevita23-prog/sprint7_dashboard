import pandas as pd
import plotly.express as px
import streamlit as st

# Encabezado
st.header("Panel interactivo - Sprint 7")

# Cargar datos con cache
@st.cache_data
def load_data(path: str):
    return pd.read_csv(path)

df = load_data("vehicles_us.csv")

# Vista previa
st.subheader("Vista previa de los datos")
st.dataframe(df.head(), use_container_width=True)
st.caption(f"Filas: {df.shape[0]:,} • Columnas: {df.shape[1]}")

# Histograma
st.subheader("Histograma")
if st.button("Construir histograma (odometer)"):
    st.write("Distribución del odómetro")
    data = df["odometer"].dropna()
    fig = px.histogram(data, x="odometer", title="Distribución del Odómetro")
    st.plotly_chart(fig, use_container_width=True)

# Gráfico de dispersión
st.subheader("Gráfico de dispersión")
if st.button("Construir dispersión (precio vs odometer)"):
    st.write("Relación Precio vs Odómetro")
    data = df[["odometer", "price"]].dropna()
    fig = px.scatter(
        data, x="odometer", y="price",
        title="Precio vs Odómetro",
        opacity=0.6
    )
    st.plotly_chart(fig, use_container_width=True)
