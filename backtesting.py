import pandas as pd
from strategy import TradingStrategy

df = pd.read_csv("trading_dataset.csv")
strategy = TradingStrategy()

profits = []
for i in range(10, len(df)):
    price_data = df.iloc[i-10:i][['open', 'high', 'low', 'close']].values.flatten()
    signal = strategy.generate_signal(price_data)
    profits.append(1 if signal == "BUY" else -1)

print(f"Total Backtesting Profit: {sum(profits)}")
