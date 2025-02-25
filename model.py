import joblib
import numpy as np

class TradingModel:
    def __init__(self):
        self.model = joblib.load("ml_model/trained_model.pkl")

    def predict(self, data):
        return self.model.predict(np.array(data).reshape(1, -1))[0]
