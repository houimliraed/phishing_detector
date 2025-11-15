from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl
import joblib
import os
from utils import extract_features


# MAKING SURE WE GET THE RIGHT PATH FOR THE MODELS

BASE_DIR = os.path.dirname(__file__)

model = joblib.load(os.path.join(BASE_DIR,"models","phishing_model.pkl"))
scaler = joblib.load(os.path.join(BASE_DIR,"models","scaler.pkl"))

app = FastAPI(title="fishing url detector API")

@app.get('/')
def root():
    return {"message":"hello from fishing url detector !"}

@app.post('/predict')
def predict(data: URLRequest):
    pass

    

@app.get('/url_test')
def url_test():
    pass



