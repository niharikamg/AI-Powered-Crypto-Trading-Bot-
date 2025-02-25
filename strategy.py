import numpy as np
from model import TradingModel

class TradingStrategy:
    def __init__(self):
        self.model = TradingModel()

    def generate_signal(self, price_data):
        prediction = self.model.predict(price_data)
        return "BUY" if prediction > price_data[-1] else "SELL"
