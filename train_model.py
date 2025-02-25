import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv("trading_dataset.csv")

# Prepare features and labels
X = df[['open', 'high', 'low', 'close']]
y = df['close'].shift(-1)

X_train, X_test, y_train, y_test = train_test_split(X[:-1], y[:-1], test_size=0.2)

# Train model
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "trained_model.pkl")
