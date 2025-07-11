# app.py
from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load trained model
model = joblib.load('fraud_detection_model.pkl')

@app.route('/')
def index():
    return render_template('index.html', prediction=None)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input from form
        features = request.form['features']
        features_list = np.array(features.split(','), dtype=float).reshape(1, -1)
        
        # Predict
        prediction = model.predict(features_list)[0]
        
        return render_template('index.html', prediction=prediction)
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
