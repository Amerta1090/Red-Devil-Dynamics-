from fastapi import APIRouter
from app.schemas.request import PredictionRequest
from app.services.prediction import predict_live
from app.models.loader import load_models

router = APIRouter()

poisson_model, avg_interval = load_models()

@router.post("/predict")

def predict(data: PredictionRequest):

    prob = predict_live(
        poisson_model,
        data.current_minute,
        data.cumulative_shots,
        data.cumulative_xG,
        data.side
    )

    return {"probability_goal_next_10_min": float(prob)}
