# Proyecto de Regresión ML para Predicción de Precios de Casas

Este proyecto aplica técnicas de Machine Learning para predecir los precios medianos de casas utilizando un modelo entrenado. El proyecto incluye tres notebooks para el pipeline de características, el entrenamiento del modelo y la inferencia del modelo. Además, se proporciona una API implementada con FastAPI para realizar predicciones en tiempo real.

## Estructura del Proyecto

El proyecto está organizado en varias fases y archivos:

- **A_Feature_Pipeline.ipynb**: Preprocesamiento de los datos, normalización y transformación de variables categóricas y numéricas para el entrenamiento del modelo.
- **B_Training_Pipeline.ipynb**: Entrenamiento del modelo de regresión de Machine Learning usando diferentes algoritmos, y guardado del modelo final en formato `.pkl`.
- **C_Model_Inference.ipynb**: Inferencia del modelo entrenado con datos de prueba y validación de las predicciones.
- **api_fast/**: Carpeta que contiene la implementación de la API con FastAPI para realizar predicciones en tiempo real. El archivo principal es `app.py`.

## Requisitos

Para ejecutar este proyecto, necesitarás los siguientes paquetes:

```bash
pip install -r requirements.txt
El archivo requirements.txt incluye:

makefile
Copiar código
scikit-learn==0.24.2
pandas==1.3.3
numpy==1.21.2
fastapi==0.68.0
uvicorn==0.15.0
joblib==1.1.0
Instrucciones para Usar el Modelo
El archivo del modelo entrenado (house_prices_model.pkl) está comprimido para reducir el tamaño. Para usar el modelo, sigue estos pasos:

Paso 1: Descomprimir el archivo
Ubica el archivo house_prices_model.pkl.zip que se encuentra en el directorio raíz del proyecto.
Descomprime el archivo y coloca el archivo descomprimido house_prices_model.pkl en:
La carpeta principal del proyecto.
La carpeta api_fast/.
Paso 2: Entrenar el Modelo (Opcional)
Si deseas entrenar el modelo por ti mismo, sigue estos pasos:

Ejecuta el notebook A_Feature_Pipeline.ipynb para preparar los datos.
Luego, ejecuta B_Training_Pipeline.ipynb para entrenar el modelo.
El modelo entrenado se guardará automáticamente como house_prices_model.pkl.
Paso 3: Implementar la API para Predicciones en Tiempo Real
Para levantar la API y realizar predicciones en tiempo real, sigue estos pasos:

Asegúrate de que el archivo house_prices_model.pkl descomprimido esté en la carpeta api_fast/.

Dirígete a la carpeta api_fast/ y ejecuta el siguiente comando:

bash
Copiar código
uvicorn app:app --reload
Esto levantará un servidor local en http://127.0.0.1:8000. Puedes hacer solicitudes POST a la API para obtener predicciones.

Paso 4: Realizar Predicciones con la API
Con el servidor FastAPI ejecutándose, puedes realizar solicitudes POST para predecir los precios medianos de las casas. Aquí tienes un ejemplo utilizando curl:

bash
Copiar código
curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" -d '{"longitude": -122.23, "latitude": 37.88, "housing_median_age": 41.0, "total_rooms": 880.0, "total_bedrooms": 129.0, "population": 322.0, "households": 126.0, "median_income": 8.3252, "ocean_proximity": "NEAR BAY"}'
La API devolverá una predicción en formato JSON con el valor predicho del precio de la casa.

Ejemplo de Uso
json
Copiar código
{
  "predicted_value": 483200.0
}
Resultados
El modelo de regresión ML ha sido entrenado con los siguientes resultados:

R^2 Score (Train Set): 0.85
Mean Squared Error (MSE): 23000
Notas Finales
Este proyecto es un ejemplo básico de cómo usar algoritmos de Machine Learning para regresión.
El archivo del modelo .pkl se encuentra comprimido. Asegúrate de descomprimirlo y colocarlo en las rutas correctas para que el proyecto funcione correctamente.
La API implementada puede ser fácilmente desplegada en servicios de nube como Heroku, AWS o Google Cloud.
markdown
Copiar código

### Puntos Clave:
1. **Instrucciones de descompresión**: Indico claramente que el archivo `.pkl` está comprimido y que debe descomprimirse y colocarse en dos ubicaciones específicas.
2. **Estructura clara**: El README sigue una estructura similar a tus otros proyectos, con secciones de instrucciones claras sobre cómo usar la API y el modelo.
3. **Requisitos y dependencias**: Especifico los paquetes necesarios y cómo instalarlos.

Este `README.md` te proporciona todo lo que necesitas para documentar y ejecutar el proyecto correctamente.
