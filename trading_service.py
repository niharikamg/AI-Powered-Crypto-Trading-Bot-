import os
from binance.client import Client

class TradingService:
    def __init__(self):
        self.client = Client(os.getenv("BINANCE_API_KEY"), os.getenv("BINANCE_SECRET_KEY"))

    def get_balance(self):
        return self.client.get_account()

    def execute_trade(self, symbol="BTCUSDT", quantity=0.01, trade_type="BUY"):
        order = self.client.order_market(symbol=symbol, side=trade_type, quantity=quantity)
        return order
