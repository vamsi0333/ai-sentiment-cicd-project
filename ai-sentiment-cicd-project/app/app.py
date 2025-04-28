from fastapi import FastAPI
import pickle
from typing import Optional

# Load model and vectorizer
with open("model.pkl", "rb") as f:
    model, vectorizer = pickle.load(f)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to AI Sentiment Analysis API!"}

@app.get("/predict/")
def predict_sentiment(text: Optional[str] = None):
    if text:
        vect_text = vectorizer.transform([text])
        prediction = model.predict(vect_text)[0]
        return {"text": text, "sentiment": prediction}
    else:
        return {"error": "Please provide text for sentiment prediction."}