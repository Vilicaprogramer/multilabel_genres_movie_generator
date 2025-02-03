# Importamos todas las librerías necesarias
import joblib
import streamlit as st
import preprocesing_txt as pp

# Cargamos el modelo de clasificación de géneros de películas
model = joblib.loac('cc_model.pkl')


