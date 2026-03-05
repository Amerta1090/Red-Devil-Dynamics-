import numpy as np
import pandas as pd
from app.config import SIMULATION_INTERVAL_STEP, MAX_PREDICTION_MINUTE

def predict_live(poisson_model, current_minute, cumulative_shots, cumulative_xG, mu_side_in_match):

    total_lambda_for_10_min = 0.0

    first_interval_end = int(np.ceil((current_minute + 1) / SIMULATION_INTERVAL_STEP) * SIMULATION_INTERVAL_STEP)
    second_interval_end = first_interval_end + SIMULATION_INTERVAL_STEP

    intervals_to_predict = []

    if first_interval_end <= MAX_PREDICTION_MINUTE:
        intervals_to_predict.append(first_interval_end)

    if second_interval_end <= MAX_PREDICTION_MINUTE:
        intervals_to_predict.append(second_interval_end)

    if not intervals_to_predict:
        return 0.0

    cum_shots = cumulative_shots
    cum_xG = cumulative_xG
    cum_fast_break = 0

    for interval_end in intervals_to_predict:

        X = pd.DataFrame([{
            'const': 1,
            'minute_interval': interval_end,
            'mu_side_in_match': mu_side_in_match,
            'cumulative_shots': cum_shots,
            'cumulative_xG': cum_xG,
            'cumulative_fast_break': cum_fast_break
        }])

        lambda_pred = poisson_model.predict(X)[0]

        total_lambda_for_10_min += lambda_pred

    return 1 - np.exp(-total_lambda_for_10_min)
