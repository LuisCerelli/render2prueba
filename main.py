# main.py
from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# @app.get("/data/{dataset_id}")
# def get_data(dataset_id: int):
#     # Validar el id del dataset
#     if dataset_id < 0 or dataset_id > 2:
#         return {"error": "Invalid dataset_id. Must be 0, 1, or 2."}
    
#     # Cargar el dataset Parquet correspondiente
#     df = pd.read_parquet(f"data_{dataset_id}.parquet")
#     return df.to_dict(orient="records")
# # ¿Qué hace el código anterior?
# # R: Define una API con FastAPI que permite acceder a tres datasets Parquet de 2 MB cada uno.

# from fastapi import Depends, FastAPI, HTTPException, status
# from typing import Dict

# # Ejemplo de almacenamiento en memoria para los datasets
# datasets_cache: Dict[int, dict] = {}

# @app.get("/data/{dataset_id}")
# def get_data(dataset_id: int):
#     # Verificar que el dataset_id esté dentro del rango esperado
#     if dataset_id < 0 or dataset_id > 2:
#         return {"error": "Invalid dataset_id. Must be 0, 1, or 2."}
    
#     # Verificar si los datos del dataset ya están en caché
#     if dataset_id in datasets_cache:
#         return datasets_cache[dataset_id]
    
#     # Cargar el dataset Parquet correspondiente y almacenarlo en caché
#     df = load_dataset(dataset_id)
#     dataset_dict = df.to_dict(orient="records")
#     datasets_cache[dataset_id] = dataset_dict
#     return dataset_dict

# def load_dataset(dataset_id: int):
#     # Implementación para cargar el dataset Parquet desde el archivo
#     pass

# from fastapi import FastAPI, HTTPException
# import pandas as pd

# app = FastAPI()

# Función para cargar y devolver el dataset Parquet
def load_dataset(dataset_id: int):
    try:
        # Ruta al archivo Parquet
        file_path = f"data_{dataset_id}.parquet"
        
        # Cargar el dataset Parquet
        df = pd.read_parquet(file_path)
        return df.to_dict(orient="records")
    except Exception as e:
        # Manejar cualquier error que pueda ocurrir al cargar el archivo Parquet
        raise HTTPException(status_code=500, detail="Error al cargar el dataset Parquet")

@app.get("/data/{dataset_id}")
def get_data(dataset_id: int):
    # Validar el id del dataset
    if dataset_id < 0 or dataset_id > 2:
        raise HTTPException(status_code=422, detail="Invalid dataset_id. Must be 0, 1, or 2.")
    
    # Cargar y devolver el dataset Parquet
    return load_dataset(dataset_id)
