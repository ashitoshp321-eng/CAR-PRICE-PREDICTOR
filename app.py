from flask import Flask, render_template, request, url_for
import joblib
import numpy as np
import pandas as pd
import os
from datetime import datetime

# File to store prediction history
PREDICTIONS_FILE = 'predictions.csv'

# Ensure predictions file exists with header
if not os.path.exists(PREDICTIONS_FILE):
    pd.DataFrame(columns=['timestamp', 'horsepower', 'enginesize', 'curbweight', 'predicted_price']).to_csv(PREDICTIONS_FILE, index=False)

# Load model
model = joblib.load("model.pkl")

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    horsepower = float(request.form['horsepower'])
    enginesize = float(request.form['enginesize'])
    curbweight = float(request.form['curbweight'])

    features = np.array([[horsepower, enginesize, curbweight]])

    prediction = model.predict(features)

    output = round(prediction[0], 2)

    # Append prediction to CSV history
    row = {
        'timestamp': datetime.now().isoformat(sep=' ', timespec='seconds'),
        'horsepower': horsepower,
        'enginesize': enginesize,
        'curbweight': curbweight,
        'predicted_price': output
    }
    pd.DataFrame([row]).to_csv(PREDICTIONS_FILE, mode='a', header=False, index=False)

    return render_template('index.html', prediction_text=f'Predicted Car Price: ₹ {output}')


@app.route('/history')
def history():
    if os.path.exists(PREDICTIONS_FILE):
        df = pd.read_csv(PREDICTIONS_FILE)
        records = df.to_dict('records')
    else:
        records = []
    return render_template('history.html', records=records)


if __name__ == "__main__":
    app.run(debug=True)