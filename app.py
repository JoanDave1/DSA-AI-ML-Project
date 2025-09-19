from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load your trained model
model = joblib.load('xgboost_fraud_model.pkl')

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        try:
            input_data = [
                float(request.form['distance_from_home']),
                float(request.form['distance_from_last_transaction']),
                float(request.form['ratio_to_median_purchase_price']),
                int(request.form['used_chip']),
                int(request.form['used_pin_number']),
                int(request.form['online_order']),
                int(request.form['repeat_retailer'])
            ]

            print("INPUT received:", input_data)

            # Predict fraud probability
            proba = model.predict_proba([input_data])[0][1]
            print("PREDICTED fraud probability:", proba)

            threshold = 0.001  # Adjust threshold to make fraud detection more sensitive
            prediction = 1 if proba >= threshold else 0
            result = "Fraud" if prediction == 1 else "Not Fraud"

        except Exception as e:
            result = f"Error: {str(e)}"

    return render_template('index.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True)
