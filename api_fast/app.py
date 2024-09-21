from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import numpy as np

# Cargar el modelo entrenado
model = joblib.load('house_prices_model.pkl')

# Inicializar la app de FastAPI
app = FastAPI()

# Definir el formato de entrada de datos
class HouseData(BaseModel):
    longitude: float
    latitude: float
    housing_median_age: float
    total_rooms: float
    total_bedrooms: float
    population: float
    households: float
    median_income: float
    ocean_proximity: str

# Lista de columnas que el modelo espera (incluye todas las categorías de ocean_proximity)
expected_columns = ['longitude', 'latitude', 'housing_median_age', 'total_rooms', 
                    'total_bedrooms', 'population', 'households', 'median_income', 
                    'ocean_proximity_<1H OCEAN', 'ocean_proximity_INLAND', 
                    'ocean_proximity_ISLAND', 'ocean_proximity_NEAR BAY', 
                    'ocean_proximity_NEAR OCEAN']

# Preprocesar los datos de entrada para la predicción
def preprocess_data(data: HouseData):
    # Convertir los datos en un DataFrame
    df = pd.DataFrame([data.dict()])
    
    # Realizar el one-hot encoding
    ocean_proximity_encoded = pd.get_dummies(df['ocean_proximity'], drop_first=False)
    
    # Eliminar la columna original
    df = df.drop(['ocean_proximity'], axis=1)
    
    # Concatenar las columnas codificadas
    df = pd.concat([df, ocean_proximity_encoded], axis=1)
    
    # Asegurar que todas las columnas esperadas estén presentes (rellenar faltantes con ceros)
    for col in expected_columns:
        if col not in df.columns:
            df[col] = 0
    
    # Ordenar las columnas para que coincidan con las esperadas por el modelo
    df = df[expected_columns]
    
    return df

# Ruta para realizar predicciones
@app.post("/predict")
async def predict(data: HouseData):
    try:
        # Preprocesar los datos de entrada
        input_data = preprocess_data(data)

        # Realizar predicción
        prediction = model.predict(input_data)

        # Devolver la predicción
        return {"predicted_value": float(prediction[0])}
    except Exception as e:
        return {"error": f"Ocurrió un error al procesar la solicitud: {e}"}

