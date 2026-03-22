from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()

# load trained model
model = joblib.load("models/churn_model.pkl")


@app.get("/")
def home():
    return {"message": "Customer Churn Prediction API"}


@app.post("/predict")
def predict_churn(tenure: int, monthly_charges: float):

    # create a row with all model features
    data = pd.DataFrame({
        "customerID":[0],
        "gender":[0],
        "SeniorCitizen":[0],
        "Partner":[0],
        "Dependents":[0],
        "tenure":[tenure],
        "PhoneService":[0],
        "MultipleLines":[0],
        "InternetService":[0],
        "OnlineSecurity":[0],
        "OnlineBackup":[0],
        "DeviceProtection":[0],
        "TechSupport":[0],
        "StreamingTV":[0],
        "StreamingMovies":[0],
        "Contract":[0],
        "PaperlessBilling":[0],
        "PaymentMethod":[0],
        "MonthlyCharges":[monthly_charges],
        "TotalCharges":[monthly_charges * tenure]
    })

    prediction = model.predict(data)

    return {"prediction": int(prediction[0])}