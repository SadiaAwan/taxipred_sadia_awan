from pathlib import Path 

BASE_PATH = Path(__file__).parents[1]  #src/taxipred

DATA_PATH = BASE_PATH / "data"
MODEL_PATH = BASE_PATH / "model_development"



TAXI_CLEANED_CSV = MODEL_PATH / "taxi_cleaned_training_data.csv"
JOBLIB_PATH = MODEL_PATH / "LM_model.joblib"

# DATA_PATH = Path(__file__).parents[1] / "data"
# MODEL_PATH = Path(__file__).parent / "model_development"


TAXI_CSV_PATH = DATA_PATH / "taxi_trip_pricing.csv"
#TAXI_CLEANED_CSV = MODEL_PATH/ "taxi_cleaned_training_data.csv"
#OBLIB_PATH = MODEL_PATH/ "LM_model.joblib"