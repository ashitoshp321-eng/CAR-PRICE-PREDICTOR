# 🚗 CAR PRICE PREDICTOR

An AI-powered Flask web application that predicts car prices using **Multiple Linear Regression**.
This project provides a modern futuristic UI where users can enter car specifications and instantly get predicted car prices using a trained machine learning model.

---

# ✨ Features

* 🚘 Predict car prices using Machine Learning
* 📊 Multiple Linear Regression model
* ⚡ Real-time prediction using Flask
* 🧠 Trained on real car dataset
* 📁 Prediction history storage using CSV
* 📜 Dedicated history page
* 🎨 Modern futuristic UI with glassmorphism
* 📱 Fully responsive design
* 🌌 Animated background effects

---

# 🛠️ Technologies Used

* Python
* Flask
* HTML5
* CSS3
* JavaScript
* Scikit-learn
* Pandas
* NumPy

---

# 📂 Project Structure

```bash
CAR-PRICE-PREDICTOR/
│
├── app.py
├── model.py
├── model.pkl
├── predictions.csv
├── requirements.txt
├── CarPrice_Assignment.csv
│
├── templates/
│   ├── index.html
│   └── history.html
│
├── static/
│   └── car-bg.jpg
│
└── README.md
```

---

# 📌 Features Overview

## 🔹 Car Price Prediction

Predicts car prices based on:

* Horsepower
* Engine Size
* Curb Weight

## 🔹 Prediction History

Stores all previous predictions inside:

```bash
predictions.csv
```

Users can view prediction history from:

```bash
/history
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/CAR-PRICE-PREDICTOR.git
```

---

## 2️⃣ Navigate to Project Folder

```bash
cd CAR-PRICE-PREDICTOR
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Application

```bash
python app.py
```

---

# 🌐 Open in Browser

```text
http://127.0.0.1:5000/
```

---

# 🧠 Train the Model Again

If you want to retrain the machine learning model:

```bash
python model.py
```

This will generate:

```bash
model.pkl
```

---

# 📷 UI Preview

The project includes:

* Futuristic car-themed background
* Neon glow effects
* Glassmorphism prediction card
* Responsive modern layout

---

# 📊 Machine Learning Model

This project uses:

```text
Multiple Linear Regression
```

### Input Features:

* Horsepower
* Engine Size
* Curb Weight

### Target:

* Car Price

---

# 📜 Example Prediction Flow

1. Enter car specifications
2. Click "Predict Price"
3. ML model predicts the estimated car price
4. Result appears instantly on screen
5. Prediction gets saved into history

---

# 🚀 Future Improvements

* Add more ML algorithms
* Deploy on Render / Railway / Heroku
* Add authentication system
* Add charts and analytics dashboard
* Add car image upload support

---

# 👨‍💻 Author

Developed by Rocky Pawar

---

# ⭐ Support

If you like this project:

* Star the repository
* Fork the project
* Share with others

---

# 📄 License

This project is open-source and available under the MIT License.
