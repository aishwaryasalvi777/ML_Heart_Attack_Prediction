# ML Heart Attack Prediction

A machine learning project that predicts heart attack risk using a Random Forest classifier. This project includes data preprocessing, model training, and deployment with both FastAPI and Streamlit interfaces.

## 📋 Project Overview

This project aims to predict whether a patient is at high or low risk of experiencing a heart attack based on various health metrics and lifestyle factors. The model is trained on a comprehensive dataset containing 21+ health-related features and deployed through multiple interfaces for easy access.

## 🎯 Objectives

- Preprocess and clean health prediction dataset
- Train a machine learning model (Random Forest) for binary classification
- Deploy the model via FastAPI backend API
- Provide user-friendly Streamlit interface for predictions
- Package the application using Docker for easy deployment

## 📊 Dataset

**File:** `heart_attack_prediction_dataset.csv`

### Features (21 attributes):
- **Patient Demographics:** Age, Sex
- **Health Metrics:** 
  - Blood Pressure (Systolic/Diastolic)
  - Cholesterol
  - Heart Rate
  - BMI
  - Triglycerides
- **Lifestyle Factors:**
  - Smoking
  - Alcohol Consumption
  - Diet
  - Exercise Hours Per Week
  - Physical Activity Days Per Week
  - Sedentary Hours Per Day
  - Sleep Hours Per Day
- **Medical History:**
  - Diabetes
  - Family History
  - Previous Heart Problems
  - Medication Use
  - Obesity
- **Socioeconomic:**
  - Income
  - Stress Level
- **Geographic:**
  - Country
  - Continent
  - Hemisphere

### Target Variable:
- **Heart Attack Risk:** Binary (0 = Low Risk, 1 = High Risk)

## 🗂️ Project Structure

```
ML_Heart_Attack_Prediction/
├── README.md                                    # Project documentation
├── Dockerfile                                   # Docker configuration
├── heart_attack_prediction_dataset.csv          # Training dataset
├── Heart_Attack_Prediction.ipynb                # Jupyter notebook with EDA & model training
├── streamlitapp.py                              # Streamlit web interface
├── app/
│   ├── fastapi/
│   │   └── main.py                              # FastAPI backend (alternative)
│   └── streamlit/
│       └── streamlitapp.py                      # Streamlit frontend (alternative)
└── deploy/
    └── fastapi/
        ├── main.py                              # FastAPI application
        ├── app.py                               # Application configuration
        ├── requirements.txt                     # Python dependencies
        ├── Dockerfile                           # Docker configuration for FastAPI
        ├── random_forest_pipeline.joblib        # Trained model pipeline
        └── __pycache__/                         # Compiled Python files
```

## 🔧 Technical Stack

- **Machine Learning:** scikit-learn
- **Data Processing:** pandas, numpy
- **Backend API:** FastAPI, uvicorn
- **Frontend Interface:** Streamlit
- **Model Serialization:** joblib
- **Containerization:** Docker
- **Language:** Python 3.9+

## 📦 Installation

### Prerequisites
- Python 3.9+
- pip or conda
- Docker (optional, for containerization)

### Local Setup

1. **Clone or download the project:**
   ```bash
   cd ML_Heart_Attack_Prediction
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r deploy/fastapi/requirements.txt
   ```

## 🚀 Running the Application

### Option 1: Streamlit Interface
Run the interactive web interface:
```bash
streamlit run streamlitapp.py
```
Access the app at `http://localhost:8501`

### Option 2: FastAPI Backend
Run the API server:
```bash
cd deploy/fastapi
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
Access the API documentation at `http://localhost:8000/docs`

### Option 3: Docker Container
Build and run using Docker:
```bash
cd deploy/fastapi
docker build -t heart-attack-prediction .
docker run -p 8000:8000 heart-attack-prediction
```

## 📝 Data Preprocessing

The data preprocessing pipeline includes:

1. **Data Cleaning:**
   - Conversion of numerical columns to appropriate data types
   - Conversion of binary columns (Yes/No) to integers (0/1)
   - Handling missing values using median/mode imputation

2. **Feature Engineering:**
   - Split Blood Pressure into Systolic and Diastolic components
   - Convert Stress Level to numeric format
   - Create derived features:
     - `Age_squared`
     - `Age_to_exercise_ratio`
     - `Exercise_hours_squared`

3. **Output:**
   - Cleaned dataset saved as `cleaned_heart_attack_prediction_dataset.csv`

## 🤖 Model Information

**Model Type:** Random Forest Classifier
- Ensemble learning method combining multiple decision trees
- Handles non-linear relationships
- Provides feature importance rankings
- Robust to outliers and overfitting

**Model Pipeline:** 
- Stored as `random_forest_pipeline.joblib`
- Includes preprocessing and classification steps
- Ready for production use

## 📡 API Endpoints

### FastAPI Backend

**Root Endpoint:**
```
GET /
Returns: {"message": "Heart Attack Risk Prediction API"}
```

**Prediction Endpoint:**
```
POST /predict
```

**Input Format (JSON):**
```json
{
  "Age": 45,
  "Cholesterol": 200.5,
  "SystolicBP": 130,
  "DiastolicBP": 85,
  "HeartRate": 72,
  "BMI": 25.5,
  "Triglycerides": 150,
  "Diabetes": 0,
  "FamilyHistory": 1,
  "PreviousHeartProblems": 0,
  "MedicationUse": 0,
  "Smoking": 1,
  "Obesity": 0,
  "AlcoholConsumption": 0,
  "ExerciseHoursPerWeek": 4.5,
  "StressLevel": 7,
  "SedentaryHoursPerDay": 6,
  "Income": 50000,
  "PhysicalActivityDaysPerWeek": 3,
  "SleepHoursPerDay": 7,
  "Country": "USA",
  "Continent": "North America",
  "Hemisphere": "Northern Hemisphere",
  "Sex": "Male",
  "Diet": "Average",
  "PatientID": "PAT001"
}
```

**Output Format (JSON):**
```json
{
  "prediction": "High Risk"  // or "Low Risk"
}
```

## 🎨 Streamlit Features

The Streamlit interface provides:
- User-friendly input forms for patient health data
- Real-time prediction display
- Configurable API connection settings
- Visual feedback for API responses
- Error handling and status messages

## 📊 Notebook Analysis

**Heart_Attack_Prediction.ipynb** includes:
- Data loading and exploration
- Exploratory Data Analysis (EDA)
- Data cleaning and preprocessing
- Feature engineering
- Model training and evaluation
- Model serialization

## 🐳 Docker Deployment

The project includes Docker configurations for containerized deployment:

**Build Image:**
```bash
docker build -t heart-attack-prediction:latest .
```

**Run Container:**
```bash
docker run -p 8000:8000 heart-attack-prediction:latest
```

The Dockerfile:
- Uses Python 3.9-slim as base image
- Installs all required dependencies
- Exposes port 8000 for API access
- Runs FastAPI application with uvicorn

## ⚙️ Dependencies

```
fastapi           # Web framework for building APIs
uvicorn           # ASGI server for FastAPI
pandas            # Data manipulation and analysis
scikit-learn      # Machine learning library
joblib            # Model serialization and loading
```

## 📈 Model Performance

The Random Forest model is evaluated based on:
- **Accuracy:** Overall prediction correctness
- **Precision:** Correctness of positive predictions
- **Recall:** Coverage of actual positive cases
- **F1-Score:** Harmonic mean of precision and recall

## 🔐 Input Validation

The FastAPI backend validates all input data using Pydantic models to ensure:
- Correct data types
- Required fields are present
- Data constraints are met (e.g., reasonable age ranges)

## 💡 Usage Examples

### Using FastAPI Directly

```python
import requests

url = "http://localhost:8000/predict"
data = {
    "Age": 50,
    "Cholesterol": 220,
    "SystolicBP": 140,
    # ... other fields
}

response = requests.post(url, json=data)
print(response.json())  # {"prediction": "High Risk"}
```

### Using Streamlit Interface

Simply run the Streamlit app and fill out the input form to get instant predictions with visual feedback.

## 📋 Requirements

See [deploy/fastapi/requirements.txt](deploy/fastapi/requirements.txt) for complete dependency list.

## 🤝 Contributing

To extend this project:
1. Improve data preprocessing techniques
2. Experiment with different ML algorithms
3. Add more health metrics to the dataset
4. Enhance the UI/UX of Streamlit interface
5. Implement model explainability features (e.g., SHAP values)

## 📄 License

This project is provided as-is for educational and healthcare prediction purposes.

## ⚠️ Disclaimer

This model is for **educational purposes only** and should not be used as a substitute for professional medical advice. Always consult with a qualified healthcare professional for actual health concerns.

## 📞 Support

For questions or issues, please refer to the project documentation or contact the development team.

---

**Last Updated:** December 2025
**Python Version:** 3.9+
**Status:** Production Ready
