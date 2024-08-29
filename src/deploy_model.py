from flask import Flask, request, jsonify
import joblib
import pandas as pd
import numpy as np

# Initialize Flask application
app = Flask(__name__)

# Load the trained model
model = joblib.load('C:/Users/Mayur/OneDrive/Documents/Projects/Predictive Maintenance for Industrial Equipment Using Machine Learning/models/random_forest_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract data from request
        data = request.get_json()

        # Check for required fields
        required_fields = ['Temperature_Mean', 'Vibration_Mean', 'Pressure_Mean', 'RPM_Mean']
        if not all(field in data for field in required_fields):
            return jsonify({'error': 'Missing fields in request'}), 400

        # Convert data to DataFrame
        input_df = pd.DataFrame([data])

        # Make predictions
        prediction = model.predict(input_df)
        probability = model.predict_proba(input_df).tolist()

        # Return prediction and probability
        response = {
            'prediction': int(prediction[0]),
            'probability': probability[0].tolist()
        }
        return jsonify(response), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
