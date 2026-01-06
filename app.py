import pandas as pd
import plotly.express as px
import streamlit as st

# Título de la aplicación
st.header('Análisis de anuncios de venta de vehículos')

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# --- SECCIÓN 1: HISTOGRAMA ---
hist_button = st.button('Construir histograma')

if hist_button:
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# --- SECCIÓN 2: GRÁFICO DE DISPERSIÓN ---
# Añadimos un botón para el gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    st.write('Gráfico de dispersión: Relación entre Odómetro y Precio')
    # Creamos la gráfica comparando kilometraje (odometer) vs precio
    fig_scatter = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig_scatter, use_container_width=True)

# --- SECCIÓN 3: GRÁFICO DE BARRAS ---
bar_button = st.button('Construir gráfico de barras')

if bar_button:
    st.write('Cantidad de vehículos por tipo')
    # Contamos cuántos autos hay de cada tipo (SUV, sedan, etc.)
    type_counts = car_data['type'].value_counts().reset_index()
    type_counts.columns = ['tipo', 'cantidad']

    fig_bar = px.bar(type_counts, x='tipo', y='cantidad')
    st.plotly_chart(fig_bar, use_container_width=True)
