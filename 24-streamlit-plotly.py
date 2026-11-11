import streamlit as st
import plotly.express as px
import pandas as pd

## Crear un dataframe de ejemplo
df = pd.DataFrame({
   'Fruta': ['Manzanas', 'Naranjas', 'Plátanos', 'Manzanas', 'Naranjas', 'Plátanos'],
   'Cantidad': [4, 1, 2, 2, 4, 5],
   'Ciudad': ['SF', 'SF', 'SF', 'Montreal', 'Montreal', 'Montreal']
})
 
 ## Agregar un cuadro de selección para elegir el tipo de gráfico
chart_type = st.selectbox('Elija un tipo de gráfico', ['Barra', 'Línea'])
 
 ## Crear el gráfico
if chart_type == 'Barra':
    fig = px.bar(df, x='Fruta', y='Cantidad', color='Ciudad', barmode='group')
elif chart_type == 'Línea':
    fig = px.line(df, x='Fruta', y='Cantidad', color='Ciudad')
 
fig.update_layout(
    title='Ventas por Ciudad',
    xaxis_title='Productos X',
    yaxis_title='Miles de unidades Y',
)

## Mostrar la figura en Streamlit
st.plotly_chart(fig, use_container_width=True)