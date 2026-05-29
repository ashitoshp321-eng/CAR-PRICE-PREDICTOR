import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Load dataset
df = pd.read_csv("CarPrice_Assignment.csv")

# Features
X = df[['horsepower', 'enginesize', 'curbweight']]

# Target
y = df['price']

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
joblib.dump(model, "model.pkl")

print("Model Saved Successfully")