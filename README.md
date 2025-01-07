Heart Disease Prediction (10-Year CHD Risk)
This project aims to predict whether a patient has a 10-year risk of developing Coronary Heart Disease (CHD). The prediction is based on various medical features such as age, gender, smoking status, blood pressure, cholesterol levels, and other factors. The classification model used in this project is Logistic Regression.

Dataset
The dataset contains the following features:

male: Gender of the patient (binary).
age: Age of the patient.
education: Education level of the patient.
currentSmoker: Whether the patient is currently smoking.
cigsPerDay: Average number of cigarettes smoked per day.
BPMeds: Whether the patient is on blood pressure medications.
prevalentStroke: Whether the patient has had a stroke before.
prevalentHyp: Whether the patient has hypertension.
diabetes: Whether the patient has diabetes.
totChol: Total cholesterol level.
sysBP: Systolic blood pressure.
diaBP: Diastolic blood pressure.
BMI: Body Mass Index.
heartRate: Heart rate of the patient.
glucose: Blood glucose level.
TenYearCHD: Target variable indicating whether the patient has a 10-year risk of Coronary Heart Disease (binary: 0 or 1).
Preprocessing
Missing values are handled by dropping rows with missing data using df.dropna(axis=0, inplace=True).
Model
The model used for classification is Logistic Regression, which is trained on the dataset to predict whether a patient will develop CHD within the next 10 years.

Data Splitting
Features (X) and target (y) are split as follows:
X = df.iloc[:, 0:15]  # Features
y = df.iloc[:, 15:16]  # Target (TenYearCHD)

Model Performance
The classification model is evaluated using several metrics:
Accuracy: 86%
Precision (class 0): 0.86
Recall (class 0): 0.99
F1-score (class 0): 0.92
Precision (class 1): 0.70
Recall (class 1): 0.08
F1-score (class 1): 0.15
Confusion Matrix:
[[925   6]
 [153  14]]
ROC-AUC Score: 0.7018

Web Application
A simple web interface is built using Flask to allow users to input their medical information and get predictions.

File Structure
app.py: Flask application that connects the model (heart_disease_model3.pkl) to the web interface.
index.html: The homepage where users input their information.
result.html: The page displaying the prediction results.
style.css: The CSS file for styling the HTML pages.
Flask Integration
The trained Logistic Regression model is saved as heart_disease_model3.pkl and loaded in the Flask application for real-time predictions.
Users can input their details on index.html, and the prediction result is displayed on result.html.

Installation
To run this project locally, follow the steps below:

Clone this repository:
git clone https://github.com/yourusername/heart-disease-prediction.git

Navigate to the project directory:
cd heart-disease-prediction

Install the required libraries:
pip install -r requirements.txt

Running the Web Application
Run the Flask application:

python app.py
Open a web browser and go to http://127.0.0.1:5000/ to access the application.

Contributing
Feel free to fork this project and submit pull requests. Contributions are welcome!

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
The dataset is based on publicly available health data for predictive modeling.
Thanks to the contributors of the dataset and open-source libraries used in this project.

![Screenshot 2024-12-31 014654](https://github.com/user-attachments/assets/3e459821-286d-4ba2-8d8f-f4d73956b3bc)
![Screenshot 2024-12-31 014702](https://github.com/user-attachments/assets/e828ae3a-5a01-4ab5-88c5-1af9cb7a145e)
![Screenshot 2024-12-31 014750](https://github.com/user-attachments/assets/fb1be0e2-f9d2-4474-969a-3d275a8c0035)
