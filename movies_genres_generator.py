# Importamos todas las librerías necesarias
import joblib
import streamlit as st
import preprocesing_txt as pp

# Cargamos el modelo de clasificación de géneros de películas
#model = joblib.load('cc_model.pkl')


# Creamos el título principal de la aplicación en Streamlit
st.title('***Generador de  de :blue[géneros]*** 🎬')
# Añadimos un subtítulo para dar la bienvenida al usuario
st.subheader('_Bienvenido a la aplicación búsqueda de géneros segun su sinopsis._')

# Explicamos el funcionamiento de la aplicación
st.write('En esta aplicación, muestra el poder del Machine Lerning para encontrar en los géneros de las películas \
         según lo que se diga en su sinopsis. ')

# Creamos un campo de texto para que el usuario ingrese su sinopsis de la película
text = st.text_input('Introduce aquí la sinopsis')
# Creamos un botón para enviar la sinopsis
button = st.button('Enviar')