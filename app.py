import numpy as np
import pandas as pd
from flask import Flask, render_template, request, redirect, url_for
import pickle
import sklearn
print(sklearn.__version__)

app = Flask(__name__)

# Load the trained model
model = pickle.load(open('heart_disease_model3.pkl', 'rb'))

# Check the scikit-learn version used for saving the model
print(model.__getstate__().get('_sklearn_version', 'Unknown'))

# Define feature names based on the model's expected input
feature_names = [
    'male','age', 'education', 'currentSmoker', 'cigsPerDay', 'BPMeds', 
    'prevalentStroke', 'prevalentHyp', 'diabetes', 'totChol', 'sysBP', 
    'diaBP', 'BMI', 'heartRate', 'glucose'
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Extract form data
    data = {
        "sex": request.form.get("sex"),
        "age": request.form.get("age"),
         # keep it as '1' or '0' directly
        "education": request.form.get("education"),
        "currentSmoker": "Yes" if request.form.get("currentSmoker") == "1" else "No",
        "cigsPerDay": request.form.get("cigsPerDay"),
        "BPMeds": "Yes" if request.form.get("BPMeds") == "1" else "No",
        "prevalentStroke": "Yes" if request.form.get("prevalentStroke") == "1" else "No",
        "prevalentHyp": "Yes" if request.form.get("prevalentHyp") == "1" else "No",
        "diabetes": "Yes" if request.form.get("diabetes") == "1" else "No",
        "totChol": request.form.get("totChol"),
        "sysBP": request.form.get("sysBP"),
        "diaBP": request.form.get("diaBP"),
        "BMI": request.form.get("BMI"),
        "heartRate": request.form.get("heartRate"),
        "glucose": request.form.get("glucose"),
    }

    # Prepare the data for the model (convert them to a list of floats)
    model_input = np.array([
        1 if data["sex"] == "1" else 0,  # Process the sex field here as 1 for Male, 0 for Female
        float(data["age"]),
       
        float(data["education"]),
        1 if data["currentSmoker"] == "Yes" else 0,
        float(data["cigsPerDay"]),
        1 if data["BPMeds"] == "Yes" else 0,
        1 if data["prevalentStroke"] == "Yes" else 0,
        1 if data["prevalentHyp"] == "Yes" else 0,
        1 if data["diabetes"] == "Yes" else 0,
        float(data["totChol"]),
        float(data["sysBP"]),
        float(data["diaBP"]),
        float(data["BMI"]),
        float(data["heartRate"]),
        float(data["glucose"]),
    ]).reshape(1, -1)
    print(f"Processed data for prediction: {model_input}")
    # Convert model_input to a DataFrame with feature names
    model_input_df = pd.DataFrame(model_input, columns=feature_names)
    print(f"Model input: {model_input_df}")
    

    # Predict the result using the model
    prediction = model.predict(model_input_df)
    print(prediction)
    # Return the result page with prediction result
    result = "High risk" if prediction[0] == 1 else "Low risk"

    return render_template('result.html', result=result, **data)

if __name__ == '__main__':
    app.run(debug=True)
