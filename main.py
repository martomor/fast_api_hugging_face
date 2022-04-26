from transformers import pipeline
from fastapi import FastAPI, HTTPException
from app.models import  PredictionRequest

sentiment_model = pipeline("sentiment-analysis")

app = FastAPI() 


@app.post("/sentiment")
def my_endpoint(request: PredictionRequest):
  if request.query_string != 'bad_word':
      sentiment = sentiment_model(request.query_string)
      response = f"Sentiment test: {request.query_string} === {sentiment}"
      return response
  else:
    raise HTTPException(status_code = 500, detail =  "API not available for this word")
