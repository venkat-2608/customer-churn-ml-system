# Customer Churn Prediction System

This project builds a machine learning system to predict whether a telecom customer will churn.  
It includes data analysis, model training, a FastAPI prediction service, and a database to store prediction results.

## Project Overview

The system performs the following steps:

- Load and explore telecom customer data
- Train a churn prediction model
- Save the trained model
- Serve predictions using a FastAPI API
- Store prediction results in a SQLite database

## Project Structure

data/ – dataset used for training  
notebooks/ – exploratory data analysis notebook  
src/ – training and evaluation scripts  
models/ – saved trained model  
app/ – FastAPI application  

Main files:

- train.py – trains the churn prediction model
- evaluate.py – evaluation utilities for the model
- predict.py – loads the model and runs predictions
- api.py – FastAPI API for predictions
- database.py – database connection setup
- models.py – database table definitions

## Model

Algorithm used:

- Logistic Regression (scikit-learn)

Model accuracy during testing:

~78%

## Running the Project

Install dependencies:

pip install -r requirements.txt

Start the API server:

python -m uvicorn app.api:app --reload

Open API documentation:

http://127.0.0.1:8000/docs

## Example Prediction

Example input:

tenure = 12  
monthly_charges = 80

Example response:

{
  "prediction": 1
}

Where:
0 → customer stays  
1 → customer churns

## Technologies Used

- Python
- Pandas
- Scikit-learn
- FastAPI
- SQLAlchemy
- SQLite

## Author

Venkat