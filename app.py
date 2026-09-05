import streamlit as st
import pandas as pd
import numpy as np
import joblib

# ======================
# LOAD MODEL
# ======================
model = joblib.load("best_model.pkl")


# ======================
# UI
# ======================
st.set_page_config(page_title="Car Price Predictor", layout="centered")

st.title("🚗 Used Car Price Prediction App")
st.write("Enter vehicle details to predict selling price")


# ======================
# INPUTS
# ======================
Make = st.text_input("Make")
Model_name = st.text_input("Model")
Body = st.text_input("Body Type")
Transmission = st.selectbox("Transmission", ["automatic", "manual"])
State = st.text_input("State")

Year = st.number_input("Year", 1990, 2025, 2015)
VehicleAge = st.number_input("Vehicle Age", 0, 50, 5)
Odometer = st.number_input("Odometer", 0.0, 500000.0, 50000.0)
MMR = st.number_input("MMR Value", 0.0, 100000.0, 15000.0)
ConditionValue = st.number_input("Condition Value", 1.0, 50.0, 30.0)

SaleYear = st.number_input("Sale Year", 2010, 2026, 2014)
SaleMonth = st.slider("Sale Month", 1, 12, 6)

AgeGroup = st.selectbox("Age Group", ["New", "Mid", "Old"])
MileageGroup = st.selectbox("Mileage Group", ["Low", "Medium", "High"])
MarketSignal = st.selectbox("Market Signal", ["Undervalued", "Fair", "Overvalued"])


# ======================
# PREDICTION BUTTON
# ======================
if st.button("Predict Price"):

    input_df = pd.DataFrame([{
        "Make": Make,
        "Model": Model_name,
        "Body": Body,
        "Transmission": Transmission,
        "State": State,
        "Year": Year,
        "VehicleAge": VehicleAge,
        "Odometer": Odometer,
        "MMR": MMR,
        "ConditionValue": ConditionValue,
        "SaleYear": SaleYear,
        "SaleMonth": SaleMonth,
        "AgeGroup": AgeGroup,
        "MileageGroup": MileageGroup,
        "MarketSignal": MarketSignal
    }])

    prediction = model.predict(input_df)[0]

    # ======================
    # FIX (important for log models if used later)
    # ======================
    # prediction = np.exp(prediction)

    st.success(f"💰 Predicted Selling Price: ${prediction:,.2f}")