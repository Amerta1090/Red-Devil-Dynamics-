import pickle
import pandas as pd

def load_models():
    with open("app/models/poisson_model.pkl", "rb") as f:
        poisson_model = pickle.load(f)

    avg_interval = pd.read_pickle("app/models/avg_interval.pkl")

    return poisson_model, avg_interval
