from pydantic import BaseModel

class PredictionRequest(BaseModel):
    current_minute: int
    cumulative_shots: int
    cumulative_xG: float
    side: int
