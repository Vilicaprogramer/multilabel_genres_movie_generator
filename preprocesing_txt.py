# Importamos todas las librerías necesarias
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import MultiLabelBinarizer
from nltk.stem import SnowballStemmer
import pandas as pd
import numpy as np
import string
import nltk
import joblib
import model_load as ml

nltk.download('stopwords')
from nltk.corpus import stopwords
stop = stopwords.words('spanish')

model = ml.model
vectorizer = ml.tfidf
mlb = ml.mlb

# Creamos función para preprocesar el texto
def preprocess_text(text):
    """ Preprocesa un texto y devuelve los géneros predichos por el modelo """

    # Eliminamos signos de puntuación
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Eliminamos números
    text = text.translate(str.maketrans('', '', string.digits))

    # Normalizamos el texto a minúsculas
    text = text.lower()

    # Eliminamos saltos de línea y espacios innecesarios
    text = text.replace('\n', ' ').replace('\r', ' ').replace('\t', ' ').strip()

    # Eliminación de Stop Words en español
    text = ' '.join([word for word in text.split() if word not in stop])

    # Normalización de caracteres especiales
    reemplazos = str.maketrans('áéíóúàèìòùäëïöüâêîôûãõñç', 'aeiouaeiouaeiouaeiouaonc')
    text = text.translate(reemplazos)

    # Reducimos las palabras a su raíz (stemming)
    stemmer = SnowballStemmer('spanish')
    text = ' '.join([stemmer.stem(word) for word in text.split()])

    # Convertimos el texto a su representación numérica usando el vectorizador ya entrenado
    X_tfidf = vectorizer.transform([text])

    # Aplicamos el modelo para obtener las probabilidades de cada género
    y_proba = model.predict_proba(X_tfidf)

    # Aplicamos la sigmoide para convertir logits a probabilidades
    y_proba_sigmoid = 1 / (1 + np.exp(-y_proba))

    # Aplicamos un umbral para convertir probabilidades a etiquetas binarias
    y_binario = (y_proba_sigmoid > 0.55).astype(int)

    # Descodificamos las etiquetas usando el MultiLabelBinarizer entrenado
    generos_predichos = mlb.inverse_transform(y_binario)

    # Devolvemos la lista de géneros predichos
    return generos_predichos[0]  # Devuelve una lista con los géneros predichos para el texto
