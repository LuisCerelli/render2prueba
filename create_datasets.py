# create_datasets.py
import pandas as pd
import numpy as np

# Crear tres datasets de 2 MB cada uno
for i in range(3):
    data = {
        "id": np.arange(100000),  # 100,000 filas
        "value": np.random.rand(100000)
    }
    df = pd.DataFrame(data)
    df.to_parquet(f"data_{i}.parquet")

print("Datasets creados")
