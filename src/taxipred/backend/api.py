from fastapi import FastAPI
import numpy as np
import joblib
from pydantic import BaseModel, Field

#from taxipred.data_processing import TaxiData
#from taxipred.utils.constants import JOBLIB_PATH

from data_processing import TaxiData
#from constants import JOBLIB_PATH
from taxipred.utils.constants import JOBLIB_PATH

# Skapa Em FastAPI

app = FastAPI()

model = joblib.load(JOBLIB_PATH)

# Pydantic-modell i SAMMA fil

class TaxiPredictionInput(BaseModel):
    passenger_count: int = Field(..., ge=1, le=6)
    trip_distance: float = Field(..., gt=0)


# Endpoint för att läsa data

@app.get("/data")
def get_data():
    data = TaxiData()
    return data.to_json()


# Prediktions-endpoint

@app.post("/predict")
def predict(input: TaxiPredictionInput):
    X = np.array([[input.passenger_count, input.trip_distance]])
    prediction = model.predict(X)
    return {"predicted_price": float(prediction[0])}
