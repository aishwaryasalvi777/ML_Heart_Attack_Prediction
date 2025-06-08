import joblib
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

# Load the saved pipeline
pipeline = joblib.load('random_forest_pipeline.joblib')

# Initialize FastAPI app
app = FastAPI()

# Define the input data model
class InputData(BaseModel):
    Age: int
    Cholesterol: float
    SystolicBP: int
    DiastolicBP: int
    HeartRate: int
    BMI: float
    Triglycerides: float
    Diabetes: int
    FamilyHistory: int
    PreviousHeartProblems: int
    MedicationUse: int
    Smoking: int
    Obesity: int
    AlcoholConsumption: int
    ExerciseHoursPerWeek: float
    StressLevel: int
    SedentaryHoursPerDay: float
    Income: int
    PhysicalActivityDaysPerWeek: int
    SleepHoursPerDay: float
    Country: str
    Continent: str
    Hemisphere: str
    Sex: str
    Diet: str
    PatientID: str

# Feature engineering to create required columns
def preprocess_input(data):
    df = pd.DataFrame([data])

    # Feature engineering
    df['Age_squared'] = df['Age'] ** 2
    df['Age_to_exercise_ratio'] = df['Age'] / df['ExerciseHoursPerWeek'].replace(0, 1e-6)
    df['Exercise_hours_squared'] = df['ExerciseHoursPerWeek'] ** 2

    # Ensure all required columns are present, adding missing columns with default values
    required_columns = [
        'Age', 'Cholesterol', 'SystolicBP', 'DiastolicBP', 'HeartRate', 'BMI', 'Triglycerides', 
        'Diabetes', 'FamilyHistory', 'PreviousHeartProblems', 'MedicationUse', 'Smoking', 'Obesity', 
        'AlcoholConsumption', 'ExerciseHoursPerWeek', 'StressLevel', 'SedentaryHoursPerDay', 'Income', 
        'PhysicalActivityDaysPerWeek', 'SleepHoursPerDay', 'Age_squared', 'Age_to_exercise_ratio', 
        'Exercise_hours_squared', 'PatientID', 'Country', 'Continent', 'Hemisphere', 'Sex', 'Diet'
    ]

    # Add missing columns with default values (e.g., 0 for numerical or empty strings for categorical)
    for col in required_columns:
        if col not in df.columns:
            if isinstance(df[col], pd.Series) and df[col].dtype == 'object':
                df[col] = ""  # Default empty string for categorical columns
            else:
                df[col] = 0  # Default 0 for numerical columns

    # Print the column names before renaming
    print("Columns before renaming:", df.columns.tolist())


    # Print the column names after renaming to verify the changes
    print("Columns after renaming:", df.columns.tolist())

    # Reorder the columns to ensure the model's expected column order
    df = df[required_columns]
    return df

# Prediction route
@app.post("/predict")
def predict(data: InputData):
    input_data = data.dict()
    processed_data = preprocess_input(input_data)
    prediction = pipeline.predict(processed_data)
    return {"prediction": "High Risk" if prediction[0] == 1 else "Low Risk"}

# Root route
@app.get("/")
def read_root():
    return {"message": "Heart Attack Risk Prediction API"}





#Test
# {
#   "Age": 45,
#   "Cholesterol": 200.5,
#   "SystolicBP": 130,
#   "DiastolicBP": 85,
#   "HeartRate": 75,
#   "BMI": 28.5,
#   "Triglycerides": 150,
#   "Diabetes": 1,
#   "FamilyHistory": 1,
#   "PreviousHeartProblems": 0,
#   "MedicationUse": 1,
#   "Smoking": 0,
#   "Obesity": 0,
#   "AlcoholConsumption": 1,
#   "ExerciseHoursPerWeek": 5.0,
#   "StressLevel": 2,
#   "SedentaryHoursPerDay": 4.0,
#   "Income": 50000,
#   "PhysicalActivityDaysPerWeek": 3,
#   "SleepHoursPerDay": 7.5,
#   "Country": "USA",
#   "Continent": "North America",
#   "Hemisphere": "Northern",
#   "Sex": "Male",
#   "Diet": "Balanced",
#   "PatientID": "12345"
# }
