# 💳 Credit Card Fraud Detection Web App

A machine learning web application that detects fraudulent credit card transactions using a trained classification model. Built with Flask and HTML, this app provides a simple user interface where users can input transaction details and get real-time fraud predictions.

---

## 🚀 Features

- 🔍 Predicts if a transaction is fraudulent or legitimate
- 📊 Built using a trained machine learning model
- 🖥️ User-friendly frontend interface (HTML + CSS)
- 🧠 Backend with Flask and scikit-learn
- 📦 Model loaded via `fraud_detection_model.pkl`

---

## 🧠 How the Model Works

This model is trained on anonymized credit card transaction data and uses key features such as transaction amount, time, and anonymized variables (like V1, V2, ..., V28) to determine if a transaction is fraudulent.

---

## 📁 Project Structure

├── app.py # Flask application
├── fraud_detection_model.pkl # Trained machine learning model
├── index.html # Frontend HTML page
├── background.png # Background image used in UI
├── README.md # Project documentation



---

## 🛠️ Requirements

Install the necessary Python packages using pip:

pip install -r requirements.txt
If requirements.txt is not available, install manually:


▶️ Running the App Locally
Clone the repository or download the files.

Run the Flask app:

python app.py
Open your browser and navigate to:

http://127.0.0.1:5000/

✅ Output
The model outputs a prediction:

0 → Legitimate Transaction

1 → Fraudulent Transaction

📌 Notes
Ensure model.pkl is in the same directory as app.py.

The web page styling uses background.png for visual enhancement.

The HTML frontend (index.html) must be correctly linked in the Flask app.

👨‍💻 Author
Aarsha

📜 License
This project is licensed under the MIT License. Feel free to use and modify it.
