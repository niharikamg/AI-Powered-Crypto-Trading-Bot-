from fastapi import FastAPI
from trading_service import TradingService

app = FastAPI()
trading_service = TradingService()

@app.post("/trade")
def execute_trade():
    return trading_service.execute_trade()

@app.get("/balance")
def get_balance():
    return trading_service.get_balance()
