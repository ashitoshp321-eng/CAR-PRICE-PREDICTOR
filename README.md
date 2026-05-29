# CAR-PRICE-PREDICTOR

A Flask web application for predicting car prices using multiple linear regression. The app lets users enter car specifications and view predicted prices plus a history of past predictions.

## Features

- Predict car price from horsepower, engine size, and curb weight
- Store prediction history in `predictions.csv`
- View prediction history on a dedicated page
- Responsive UI with background image styling

## Files

- `app.py` - Flask application with routes for prediction and history
- `model.py` - Trains the linear regression model and saves it as `model.pkl`
- `CarPrice_Assignment.csv` - Dataset used for model training
- `templates/index.html` - Main prediction page
- `templates/history.html` - Prediction history page
- `static/car-bg.jpg` - Background image used in the UI
- `predictions.csv` - Saved predictions history

## Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the app:

```bash
python app.py
```

3. Open the browser at:

```text
http://127.0.0.1:5000/
```

## Notes

- If you need to retrain the model, run `python model.py`.
- Make sure `model.pkl` is present before starting the Flask app.
- The history page is available at `/history`.
