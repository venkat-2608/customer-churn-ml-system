import joblib
import pandas as pd

model = joblib.load("models/churn_model.pkl")
print("Model loaded successfully")