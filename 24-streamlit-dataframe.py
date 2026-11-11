import streamlit as st
import pandas as pd
import numpy as np

loaded = False
data = {
    'Fruit': ['Manzana', 'Plátano', 'Cereza', 'Dátil', 'Baya de saúco'],
    'Cantidad': [10, 15, 20, 25, 30],
    'Precio': [0.5, 0.25, 0.75, 1.0, 2.0]
}
df = pd.DataFrame(data)

st.dataframe(df)
st.dataframe(df.style.highlight_max(axis=0))
#-----------------


# values = st.slider("Select a range of values", 0.0, 100.0, (25.0, 75.0))
# st.write("Values:", values)


cols = 5
rows = 200

df2 = pd.DataFrame(np.random.randint(0, 1000, (rows, cols)),
             columns=['A', 'B', 'C', 'D', 'E'])


columna = st.selectbox('Seleccionar columna para filtrar', df2.columns)
valor_min = st.number_input("Valor mínimo")
valor_max = st.number_input("Valor máximo")

if valor_max > valor_min :
    df_filtrado = df2[(df2[columna] >= valor_min) & (df2[columna] <= valor_max)]
else :
    df_filtrado = df2    
st.dataframe(df_filtrado, height=300)