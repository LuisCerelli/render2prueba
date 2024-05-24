# main.py
from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/data/{dataset_id}")
def get_data(dataset_id: int):
    # Validar el id del dataset
    if dataset_id < 0 or dataset_id > 2:
        return {"error": "Invalid dataset_id. Must be 0, 1, or 2."}
    
    # Cargar el dataset Parquet correspondiente
    df = pd.read_parquet(f"data_{dataset_id}.parquet")
    return df.to_dict(orient="records")
