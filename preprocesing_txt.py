# Importamos todas las librerías necesarias
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import string
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
stop = stopwords.words('spanish')

# Creamos función para preprocesar el texto
def preprocess_text(text):
    # Eliminamos los signos de puntuación.
    for punctuation in string.punctuation:
      text = text.replace(punctuation, '')
    
    # Eliminamos los números
    for numero in string.digits:
      text = text.replace(numero, '')
    
    # Normalizamos el texto a minúsculas
    text = text.lower()

    # Eliminamos posibles saltos de páginas y espacios innecesarios
    text = text.replace('\n', ' ').replace('\r', ' ').replace('\t', ' ')
    text = text.strip()

    # Eliminación de Stop Words en español
    text = ' '.join([word for word in text.split() if word not in (stop)])
    
    # Normalización de tildes, acentos raros y la ñ por n
    text = text.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')
    text = text.replace('à', 'a').replace('è', 'e').replace('ì', 'i').replace('ò', 'o').replace('ù', 'u')
    text = text.replace('ä', 'a').replace('ë', 'e').replace('ï', 'i').replace('ö', 'o').replace('ü', 'u')
    text = text.replace('â', 'a').replace('ê', 'e').replace('î', 'i').replace('ô', 'o').replace('û', 'u')
    text = text.replace('ã', 'a').replace('õ', 'o').replace('ñ', 'n').replace('ç', 'c')

    # Reducimos las palabras a su lexema con stemming
    stemmer = SnowballStemmer('spanish')
    text = ' '.join([stemmer.stem(word) for word in text.split()])

    # Eliminamos los términos con frecuencias muy altas o bajas
# Obtener palabras únicas y sus frecuencias
vocabulario = vectorizer3.get_feature_names_out()
frecuencias = count_vectorizer3.sum(axis=0).A1  # Sumar las frecuencias de cada palabra en el corpus

# Crear un DataFrame para analizar la frecuencia de las palabras
df_vocab = pd.DataFrame({'palabra': vocabulario, 'frecuencia': frecuencias})
df_vocab = df_vocab.sort_values(by='frecuencia', ascending=False)

# Buscamos las palábras que tienen una frecuencia menor de 4
baja_freq= df_vocab[df_vocab['frecuencia'] < 4]['palabra'].to_list()

# Eliminamos todas las palabras que hemos metido en la lista de baja frecuencia
text = ' '.join([word for word in text.split() if word not in (baja_freq)])

return text