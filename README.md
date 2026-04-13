# 🫀 Heart Disease Prediction (10-Year CHD Risk)

This project aims to predict whether a patient has a 10-year risk of developing Coronary Heart Disease (CHD). A simple, interactive web interface built with Flask allows users to input their medical information and receive real-time predictions powered by a Logistic Regression model.

## 📊 Dataset & Features
The model is trained on a dataset containing the following medical features:
* **male:** Gender of the patient (binary)
* **age:** Age of the patient
* **education:** Education level of the patient (1 to 4)
* **currentSmoker:** Whether the patient is currently smoking
* **cigsPerDay:** Average number of cigarettes smoked per day
* **BPMeds:** Whether the patient is on blood pressure medications
* **prevalentStroke:** Whether the patient has had a stroke before
* **prevalentHyp:** Whether the patient has hypertension
* **diabetes:** Whether the patient has diabetes
* **totChol:** Total cholesterol level (mg/dL)
* **sysBP:** Systolic blood pressure (mmHg)
* **diaBP:** Diastolic blood pressure (mmHg)
* **BMI:** Body Mass Index
* **heartRate:** Heart rate of the patient (bpm)
* **glucose:** Blood glucose level (mg/dL)

**Target Variable:** `TenYearCHD` (binary: 0 for low risk, 1 for high risk).

## ⚙️ Preprocessing & Modeling
* **Handling Missing Data:** Rows with missing values were handled using `df.dropna(axis=0, inplace=True)`.
* **Model Selection:** The classification model used is Logistic Regression.
* **Data Splitting:** * `X = df.iloc[:, 0:15]` (Features)
    * `y = df.iloc[:, 15:16]` (Target)

### Model Performance Metrics
* **Accuracy:** 86%
* **ROC-AUC Score:** 0.7018
* **Confusion Matrix:** `[[925, 6], [153, 14]]`

**Class 0 (Low Risk):**
* Precision: 0.86 | Recall: 0.99 | F1-score: 0.92
**Class 1 (High Risk):**
* Precision: 0.70 | Recall: 0.08 | F1-score: 0.15

> **Note on Model Limitations:** While overall accuracy is high, the recall for Class 1 is low due to class imbalance in the training dataset. Future improvements will include implementing over-sampling techniques (like SMOTE) or adjusting class weights to prioritize identifying positive cases of CHD.

## 💻 Web Application Structure
* `app.py`: The Flask application connecting the trained model (`heart_disease_model3.pkl`) to the web interface.
* `index.html`: The frontend form for user input.
* `result.html`: Displays the final prediction.
* `style.css`: Styling for the HTML pages.

## 🚀 Installation & Usage

To run this project locally, follow these steps:

1. **Clone this repository:**
   ```bash
   git clone [https://github.com/MutasimAlatawneh/heart-disease-prediction.git](https://github.com/MutasimAlatawneh/heart-disease-prediction.git)
   cd heart-disease-prediction
