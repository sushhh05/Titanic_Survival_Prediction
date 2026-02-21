import streamlit as st
import joblib

model = joblib.load('titanic_random_forest_model.pkl')

st.title("🚢 Titanic Survival Prediction")

st.write("Enter the details of the passenger.")

Pclass = st.selectbox("Passenger Class (1, 2, 3)", [1, 2, 3])

Sex = st.selectbox("Sex", ["male", "female"])
sex = 1 if Sex == "male" else 0

Age = st.number_input("Age", min_value=0, max_value=100, value=30)

FamilySize = st.number_input("Family Size", min_value=0, max_value=10, value=1)

Fare = st.number_input("Fare", min_value=0.0,max_value=600.00, value=32.00)

Embarked = st.selectbox("Port of Embarkation", ["C", "Q", "S"])
embarked_mapping = {"C": 0, "Q": 1, "S": 2}
embarked = embarked_mapping[Embarked] 

if st.button("Predict"):
    # Preprocess input data
    input_data = [[Pclass, sex, Age, FamilySize, Fare, embarked]]
    
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.success("🎉 The passenger would SURVIVE!")
    else:
        st.error("💀 The passenger would NOT survive.")