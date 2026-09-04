import joblib
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "final_xgb_model.pkl"
THRESHOLD_PATH = BASE_DIR / "models" / "fraud_threshold.pkl"


model = joblib.load("models/final_xgb_model.pkl")
threshold = joblib.load("models/fraud_threshold.pkl")

def predict_transaction(transaction):
    transaction_df = pd.DataFrame([transaction])

    fraud_probability = float(
        model.predict_proba(transaction_df)[:, 1][0]
    )

    prediction = int(fraud_probability >= threshold)

    if prediction == 1:
        label = "FRAUD"
    else:
        label = "LEGITIMATE"

    return {
        "fraud_probability": fraud_probability,
        "prediction": prediction,
        "label": label
    }