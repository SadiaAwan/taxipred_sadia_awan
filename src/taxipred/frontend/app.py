import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Taxi Price Predictor", layout="centered")

st.title("🚕 Taxi Price Prediction")
st.write("Fyll i reseinformation och få ett prisförslag.")

# ---- Input fields ----
distance = st.number_input(
    "Trip Distance (km)", min_value=0.0, value=5.0, step=0.1
)

duration = st.number_input(
    "Trip Duration (minutes)", min_value=0.0, value=15.0, step=1.0
)

time_of_day = st.selectbox(
    "Time of Day",
    ["Morning", "Afternoon", "Evening", "Night"]
)

passengers = st.number_input(
    "Passenger Count", min_value=1, max_value=10, value=1, step=1
)

# ---- Predict button ----
if st.button("Predict Price"):
    payload = {
        "Trip_Distance_km": distance,
        "Trip_Duration_Minutes": duration,
        "Time_of_Day": time_of_day,
        "Passenger_Count": passengers,
    }

    try:
        response = requests.post(
            f"{API_URL}/predict", json=payload, timeout=5
        )

        if response.status_code == 200:
            prediction = response.json()["prediction"]
            st.success(f"💰 Estimated Trip Price: {prediction:.2f}")
        else:
            st.error(f"API error: {response.text}")

    except requests.exceptions.RequestException as e:
        st.error("Could not connect to backend API")
