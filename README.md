# 📌 Proyecto de Clasificación de Géneros de Películas

¡Bienvenido a nuestro proyecto de Machine Learning para la clasificación automática de géneros cinematográficos a partir de sinopsis! 📽️🎬

---

## 🚀 Clonación y Ejecución del Proyecto

### 🔹 **Requisitos Previos**
Antes de comenzar, asegúrate de tener instalado:
- Python 3.8 o superior
- Git
- pip (gestor de paquetes de Python)

### 🔹 **Clonar el Repositorio**
Ejecuta el siguiente comando en tu terminal:
```bash
git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio
```

### 🔹 **Crear un Entorno Virtual (Opcional pero Recomendado)**
```bash
python -m venv venv
source venv/bin/activate  # En Windows usa: venv\Scripts\activate
```

### 🔹 **Instalar Dependencias**
```bash
pip install -r requirements.txt
```

### 🔹 **Ejecutar el Modelo**
Para predecir los géneros de una película a partir de su sinopsis, ejecuta:
```bash
streamlit run movies_genres_generator.py
```
Esto te abrirá una web donde podrás introducir la sinopsis.

---

## 🛠️ Funcionamiento del Programa

El programa toma una sinopsis de película y predice sus géneros utilizando un modelo de Machine Learning basado en técnicas de procesamiento de lenguaje natural (NLP).

### 🔹 **Proceso de Predicción**
1. **Preprocesamiento:**
   - Limpieza del texto (eliminación de signos de puntuación, números, stopwords, etc.).
   - Normalización del texto (stemming y conversión a minúsculas).
   - Conversión del texto en una representación numérica (TF-IDF).

2. **Predicción:**
   - Se carga un modelo previamente entrenado.
   - Se realiza la inferencia para obtener la probabilidad de cada género.
   - Se aplica un umbral (0.55) para asignar los géneros más probables.

3. **Salida:**
   - Devuelve una lista con los géneros predichos.

## 📁 Estructura del proyecto
```
📂 movies_genres_generator
│── .gitignore                    # Archivos y carpetas ignoradas por Git
│── README.md                      # Documentación del proyecto
│── requirements.txt                # Dependencias necesarias
│── movies_genres_generator.py      # Script principal
│── model_load.py                   # Carga del modelo entrenado
│── preprocesing_txt.py             # Preprocesamiento del texto
│── Preprocesamiento - Texto.ipynb  # Notebook con análisis y pruebas
```

### 💡 **Contribuciones**
Si deseas contribuir, por favor abre un _Pull Request_ o reporta un _Issue_. ¡Toda ayuda es bienvenida! 🚀

### 📩 **Contacto**
Si tienes alguna duda o sugerencia, no dudes en escribirme a: [vilicaprogramer@gmail.com](mailto:vilicaprogramer@gmail.com) 😊


