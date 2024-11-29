from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import pickle

# Initialize Flask app
app = Flask(__name__)

# Load the trained model using pickle
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# List of features for the model
features = ["age", "sex", "cp", "trestbps", "chol", "fbs", "restecg", "thalach", "exang", "oldpeak", "slope", "ca", "thal"]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Collect data from form and dynamically convert to int or float
        user_input = []
        
        # Dynamically convert to int or float
        for feature in features:
            value = request.form[feature]
            # Add value to user_input with appropriate type conversion
            user_input.append(float(value) if '.' in value else int(value))

        # Convert to numpy array and reshape for prediction
        input_data_as_numpy_array = np.asarray(user_input).reshape(1, -1)
        input_data_df = pd.DataFrame(input_data_as_numpy_array, columns=features)
        
        # Make prediction
        prediction = model.predict(input_data_df)
        
        # Display the result
        if prediction[0] == 0:
            prediction_text = "The person does not have heart disease."
        else:
            prediction_text = "The person has heart disease or has very high risk."
        
        return render_template('index.html', prediction=prediction_text)

    return render_template('index.html', prediction=None)

if __name__ == '__main__':
    app.run(debug=True)
