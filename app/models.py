from pydantic import BaseModel

class PredictionRequest(BaseModel):
  query_string: str