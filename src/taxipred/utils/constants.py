from pathlib import Path 

DATA_PATH = Path(__file__).parents[1] / "data"

TAXI_CSV_PATH = DATA_PATH / "taxi_trip_pricing.csv"

MODEL_PATH = Path(__file__).parent / "model_development"

JOBLIB_PATH = MODEL_PATH/ "LM_model.joblib"