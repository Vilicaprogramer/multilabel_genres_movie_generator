import gdown
import joblib

# ID del archivo en Google Drive
file_id = "1xbmt8qIzt1HixWo0e8uspNqzm1Y6ouT0"
file_id_mlb = "1GJL1Ekn9puvGuzkZjJrJVq4IrncCRDTm"
file_id_tfidf = "1KLpAI82Thrl2gkyu4tsv3gFaDR9o5eth"
url = f"https://drive.google.com/uc?id={file_id}&confirm=t"
url_mlb = f"https://drive.google.com/uc?id={file_id_mlb}&confirm=t"
url_tfidf = f"https://drive.google.com/uc?id={file_id_tfidf}&confirm=t"

# Descargar el archivo localmente
output = "modelo.pkl"
output_mlb = "mlb.pkl"
output_tfidf = "tfidf_vectorizer.pkl"
gdown.download(url, output, quiet=False)
gdown.download(url_mlb, output_mlb, quiet=False)
gdown.download(url_tfidf, output_tfidf, quiet=False)

# Cargar el modelo
model = joblib.load(output)
mlb = joblib.load(output_mlb)
tfidf = joblib.load(output_tfidf)
print("Modelos cargados correctamente.")