import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv') #Leer archivo cvs de los automoviles.
st.header("Datos de vehiculos") #Titulo del archivo.
hist_button = st.button("Construir histograma") #Boton del histograma.

if hist_button: #Presionar este boton.
    st.write ("Creacion de histograma para mostrar los tipos de autos") #Escribir este mensaje.
    fig = px.histogram(car_data, x = "type") 
    #Mostrar una grafica de histograma con los diferentes tipos de vehiculos.
    st.plotly_chart (fig, use_container_width= True) #Mostrar grafico plotly interactivo.

dispersion_button = st.button("Construir dispersion") #Boton de dispercion.

if dispersion_button: #Presionar este boton.
    st.write ("Creacion de grafica de dispercion para mostrar tipos y costos de autos") #Escribir mensaje.
    fig = px.scatter (car_data, x = "type", y = "price")
     #Mostrar una grafica de dispercion de los tipos y costos de vehiculos.
    st.plotly_chart (fig, use_container_width= True)
    fig.show()