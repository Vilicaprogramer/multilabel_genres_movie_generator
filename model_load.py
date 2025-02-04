import gdown
import joblib

# ID del archivo en Google Drive
file_id = "1xbmt8qIzt1HixWo0e8uspNqzm1Y6ouT0"
url = f"https://drive.google.com/uc?id={file_id}&confirm=t"

# Descargar el archivo localmente
output = "modelo.pkl"
gdown.download(url, output, quiet=False)

# Cargar el modelo
modelo = joblib.load(output)
print("Modelo cargado correctamente.")