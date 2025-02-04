import requests
import joblib
import streamlit as st
import io
import preprocesing_txt as pp

# ID del archivo en Google Drive
file_id = "1xbmt8qIzt1HixWo0e8uspNqzm1Y6ouT0"
url = f"https://drive.google.com/uc?export=download&id={file_id}"

# Iniciar sesión para manejar redirecciones de Google Drive
session = requests.Session()
response = session.get(url, stream=True)

# Si Google Drive envía una página HTML en lugar del archivo, obtenemos la confirmación
if "text/html" in response.headers.get("Content-Type", ""):
    # Google Drive puede requerir confirmación para archivos grandes
    for key, value in response.cookies.items():
        if "download_warning" in key:
            confirm_url = f"https://drive.google.com/uc?export=download&id={file_id}&confirm={value}"
            response = session.get(confirm_url, stream=True)
            break

# Guardamos el contenido en memoria
file_stream = io.BytesIO(response.content)

try:
    # Intentamos cargar el modelo
    modelo = joblib.load(file_stream)
    st.write("Modelo cargado correctamente")
except Exception as e:
    st.write(f"Error al cargar el modelo: {e}")


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

