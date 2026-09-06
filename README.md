# Financial Fraud Detection System

An end-to-end machine learning project for detecting fraudulent credit card transactions using XGBoost, SHAP explainability, FastAPI, React, and cloud deployment.

## Live Demo

Frontend:  
https://fraud-detection-xgb.netlify.app

Backend API:  
https://financial-fraud-detector-api.onrender.com

Swagger API Docs:  
https://financial-fraud-detector-api.onrender.com/docs

## Project Overview

This project detects potentially fraudulent credit card transactions using transaction-level features.

The system includes:

- Data preprocessing and model training
- Handling highly imbalanced classification data
- Validation-based threshold tuning
- XGBoost-based fraud detection
- SHAP explainability
- FastAPI backend
- Pydantic input validation
- React frontend dashboard
- Cloud deployment

## Model Performance

Final model: **XGBoost**

Final decision threshold: **0.20**

Final test-set fraud-class performance:

- Precision: **0.90**
- Recall: **0.84**
- F1-score: **0.87**
- PR-AUC: **~0.85**

Final confusion matrix:

```text
TN = 56855
FP = 9
FN = 16
TP = 82

The final threshold was selected using a separate validation set and was not changed after evaluating the final test set.

Why Threshold Tuning?

The dataset is highly imbalanced, with fraudulent transactions representing only around 0.17% of the total data.

Using the default probability threshold of 0.50 was not optimal for fraud detection.

A threshold of 0.20 was selected using validation data to improve fraud recall while maintaining high precision.

SHAP Explainability

SHAP was used to understand how different features influence model predictions.

The project includes:

Global feature importance
SHAP beeswarm analysis
Individual transaction explanations
SHAP waterfall plots

This helps explain why the model classifies a transaction as fraudulent or legitimate.

Note: Features V1 to V28 are anonymized PCA-transformed features from the original dataset.

Tech Stack
Machine Learning
Python
Pandas
NumPy
Scikit-learn
XGBoost
SHAP
Joblib
Backend
FastAPI
Pydantic
Uvicorn
Frontend
React
Vite
JavaScript
Deployment
Render - FastAPI backend
Netlify - React frontend
GitHub - Version control
System Architecture
User
  |
  v
React Frontend
  |
  | POST /predict
  v
FastAPI Backend
  |
  v
Pydantic Validation
  |
  v
Prediction Function
  |
  v
XGBoost Model
  |
  v
Threshold = 0.20
  |
  v
Fraud Probability + Prediction
  |
  v
React Dashboard
API Endpoint
POST /predict

The API accepts 30 numeric transaction features:

Time
V1 to V28
Amount

Example response:

{
  "fraud_probability": 0.0000040365,
  "prediction": 0,
  "label": "LEGITIMATE"
}

Possible labels:

FRAUD
LEGITIMATE
Project Structure
financial-fraud-detection/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── models/
│   ├── final_xgb_model.pkl
│   └── fraud_threshold.pkl
│
├── notebooks/
│   └── data-understanding.ipynb
│
├── src/
│   └── predict.py
│
└── frontend/
    ├── src/
    ├── index.html
    ├── package.json
    ├── package-lock.json
    └── vite.config.js
Dataset

Dataset used:

Kaggle Credit Card Fraud Detection Dataset

Features:

Time
V1 to V28
Amount
Class

Target:

0 = Legitimate
1 = Fraud

The dataset contains approximately:

284,315 legitimate transactions
492 fraudulent transactions

The raw dataset is not included in this repository.

Running the Backend Locally

Install dependencies:

pip install -r requirements.txt

Run FastAPI:

uvicorn app:app --reload

Open Swagger docs:

http://127.0.0.1:8000/docs
Running the Frontend Locally

Move into the frontend directory:

cd frontend

Install dependencies:

npm install

Run the development server:

npm run dev

Then open the local Vite URL shown in the terminal.

Deployment

The backend is deployed using Render.

The frontend is deployed using Netlify.

The deployed React frontend communicates with the deployed FastAPI backend through the /predict endpoint.

Key Learning Outcomes

This project helped me understand and implement:

Handling highly imbalanced datasets
Precision, recall, F1-score, and PR-AUC
Class weighting and SMOTE
Random Forest and XGBoost comparison
Validation-based threshold tuning
SHAP model explainability
Saving and loading trained ML models
Building prediction pipelines
Creating REST APIs using FastAPI
Request validation using Pydantic
Connecting a React frontend with an ML backend
Deploying a complete machine learning application
Disclaimer

This project is built for educational and portfolio purposes only.

It should not be used as a production financial decision-making or fraud detection system without additional validation, security, monitoring, and domain-specific controls.