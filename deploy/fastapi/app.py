import streamlit as st
import requests

# Set the FastAPI endpoint URL
FASTAPI_URL = "http://localhost:8000/predict"  # Correct API URL

# Streamlit app title and description
st.title("Heart Attack Risk Prediction")
st.write("This app interacts with a deployed FastAPI model to predict heart attack risk based on user inputs.")

# Input fields for user data
age = st.number_input("Age", min_value=1, max_value=120, value=30)
sex = st.selectbox("Sex", ["Male", "Female"])
cholesterol = st.number_input("Cholesterol (mg/dL)", min_value=100, max_value=400, value=200)
systolic_bp = st.number_input("Systolic Blood Pressure (mmHg)", min_value=80, max_value=200, value=120)
diastolic_bp = st.number_input("Diastolic Blood Pressure (mmHg)", min_value=40, max_value=120, value=80)
heart_rate = st.number_input("Heart Rate (bpm)", min_value=40, max_value=200, value=70)
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0)
triglycerides = st.number_input("Triglycerides (mg/dL)", min_value=50, max_value=500, value=150)
diabetes = st.selectbox("Diabetes", [0, 1])
family_history = st.selectbox("Family History of Heart Disease", [0, 1])
smoking = st.selectbox("Smoking Status", [0, 1])
obesity = st.selectbox("Obesity Status", [0, 1])
alcohol_consumption = st.slider("Alcohol Consumption (drinks/day)", min_value=0, max_value=10, value=2)
exercise_hours_per_week = st.slider("Exercise Hours Per Week", min_value=0.0, max_value=20.0, value=3.5)
diet = st.selectbox("Diet Type", ["Healthy", "Average", "Unhealthy"])
previous_heart_problems = st.selectbox("Previous Heart Problems", [0, 1])
medication_use = st.selectbox("Medication Use", [0, 1])
stress_level = st.slider("Stress Level (1-10)", min_value=1, max_value=10, value=5)
sedentary_hours_per_day = st.slider("Sedentary Hours Per Day", min_value=0.0, max_value=24.0, value=8.0)
country = st.selectbox("Country", ["USA", "India", "UK", "Canada"])  # Customize as per your dataset
continent = st.selectbox("Continent", ["North America", "Asia", "Europe", "Oceania"])  # Customize as per your dataset
hemisphere = st.selectbox("Hemisphere", ["Northern", "Southern"])  # Customize as per your dataset

# Submit button
if st.button("Predict Heart Attack Risk"):
    # Prepare the input data for the API request
    input_data = {
        "Age": age,
        "Sex": sex,
        "Cholesterol": cholesterol,
        "SystolicBP": systolic_bp,
        "DiastolicBP": diastolic_bp,
        "HeartRate": heart_rate,
        "BMI": bmi,
        "Triglycerides": triglycerides,
        "Diabetes": diabetes,
        "FamilyHistory": family_history,
        "Smoking": smoking,
        "Obesity": obesity,
        "AlcoholConsumption": alcohol_consumption,
        "ExerciseHoursPerWeek": exercise_hours_per_week,
        "Diet": diet,
        "PreviousHeartProblems": previous_heart_problems,
        "MedicationUse": medication_use,
        "StressLevel": stress_level,
        "SedentaryHoursPerDay": sedentary_hours_per_day,
        "Country": country,
        "Continent": continent,
        "Hemisphere": hemisphere,
        "Income": 50000,
        "PhysicalActivityDaysPerWeek": 3,
        "SleepHoursPerDay": 7.5,
        "PatientID": "12345"  # You can dynamically generate this or keep as placeholder
    }

    # Make a POST request to the FastAPI endpoint
    try:
        response = requests.post(FASTAPI_URL, json=input_data)

        if response.status_code == 200:
            prediction = response.json()
            # Assuming the response has a field 'prediction' with risk value (update as per your FastAPI response)
            risk_message = prediction.get("prediction", "Error in prediction.")
            st.success(f"Prediction: {risk_message}")
        else:
            st.error(f"Error: {response.status_code} - {response.text}")
    except Exception as e:
        st.error(f"An error occurred: {e}")

import streamlit as st

st.title("Heart Attack Risk Prediction")
st.write("This app interacts with a deployed FastAPI model to predict heart attack risk based on user inputs.")

# Check if the page loads correctly
st.write("Streamlit is running properly.")
