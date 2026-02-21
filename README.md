🚢 Titanic Survival Prediction using Machine Learning


📌 Project Overview

This project predicts whether a passenger survived the Titanic disaster using supervised machine learning algorithms.

The final model is deployed as an interactive Streamlit Web Application.

📊 Dataset Information

Source: Kaggle Titanic Dataset (train.csv)

Total Records: 891 passengers

Target Variable: Survived

Problem Type: Binary Classification

🛠 Features Used
Feature	Description
Pclass	Passenger Class (1st, 2nd, 3rd)
Sex	Gender of passenger
Age	Passenger age
SibSp	Siblings/Spouses aboard
Parch	Parents/Children aboard
Fare	Ticket fare
Embarked	Port of Embarkation
🔄 Data Preprocessing

Handling missing values

Label Encoding (Sex, Embarked)

Feature Scaling (StandardScaler for Logistic Regression)

Train-Test Split (80/20)

🤖 Models Implemented & Compared
Model	Accuracy
Logistic Regression	- 82%
KNN - 80%
Random Forest	- 84%
🏆 Best Model:

RandomForest Performed Best Out Of This.

📈 Evaluation Metrics

Accuracy Score

Confusion Matrix

Precision

Recall

F1-Score

Example Confusion Matrix:

[[92 13]
 [19 55]]

🌐 Streamlit Web Application

Interactive web app built using Streamlit.

▶ Run Locally
python -m streamlit run app.py


App will open at:

http://localhost:8501

💾 Model Saving

Model saved using:

import joblib
joblib.dump(model, "titanic_model.pkl")

📂 Project Structure
Titanic-Survival-Prediction/
│
├── train.csv
├── app.py
├── titanic_model.pkl
├── notebook.ipynb
├── requirements.txt
└── README.md

🚀 Technologies Used

Python

Pandas

NumPy

Scikit-learn

Streamlit

Joblib

🎯 Key Learning Outcomes

✔ Data Cleaning & Feature Engineering
✔ Avoiding Data Leakage
✔ Model Comparison
✔ Hyperparameter Tuning
✔ Model Deployment
✔ Building ML Web Apps

👨‍💻 Author

Sushant Nigadi
Machine Learning Enthusiast 🚀
