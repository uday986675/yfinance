import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"  # Disable GPU
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"   # Suppress TF warnings

from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import uvicorn
from tensorflow.keras.models import load_model

# Init FastAPI
app = FastAPI()

# Load model once
model = load_model("/home/uday/Documents/projects/deployment/yfinance/yfinance.keras")

# Warmup (so first request is fast)
model.predict(np.zeros((1, 80, 2)))

# Input schema
class InputData(BaseModel):
    series: list

@app.post("/predict")
def predict(data: InputData):
    if len(data.series) != 80:
        return {"error": f"Expected 80 values, got {len(data.series)}"}
    
    X = np.array(data.series).reshape(1, 80, 2)
    y_pred = model.predict(X, verbose=0)
    return {"prediction": float(y_pred[0][0])}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)