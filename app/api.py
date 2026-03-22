from fastapi import FastAPI
import joblib
import pandas as pd

from .database import engine, SessionLocal
from .models import Base, Prediction

app = FastAPI()

Base.metadata.create_all(bind=engine)

model = joblib.load("models/churn_model.pkl")


@app.get("/")
def home():
    return {"message": "Customer Churn Prediction API"}


@app.post("/predict")
def predict_churn(tenure: int, monthly_charges: float):

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
        "TotalCharges":[tenure * monthly_charges]
    })

    prediction = model.predict(data)

    db = SessionLocal()

    record = Prediction(
        tenure=tenure,
        monthly_charges=monthly_charges,
        prediction=int(prediction[0])
    )

    db.add(record)
    db.commit()
    db.close()

    return {"prediction": int(prediction[0])}