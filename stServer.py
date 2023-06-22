import streamlit as st
import requests

API_ENDPOINT = "http://localhost:5000/predict"  # Replace with the actual API endpoint URL

def make_prediction(age, sex, cigsPerDay, totChol, sysBP, glucose):
    data = {
        'age': str(age),
        'sex': str(sex),
        'cigsPerDay': str(cigsPerDay),
        'totChol': str(totChol),
        'sysBP': str(sysBP),
        'glucose': str(glucose)
    }

    response = requests.post(API_ENDPOINT, data=data)
    
    try:
        parsed_response = response.json()
        prediction = parsed_response.get('prediction')
        if prediction is None:
            raise KeyError
    except (ValueError, KeyError):
        prediction = "Error: Invalid response format"

    return prediction

# Streamlit app
st.title("Heart Disease Prediction")

# Input form
age = st.number_input("Age", value=0)
sex = st.number_input("Sex", value=0)
cigsPerDay = st.number_input("Cigarettes Per Day", value=0)
totChol = st.number_input("Total Cholesterol", value=0)
sysBP = st.number_input("Systolic Blood Pressure", value=0)
glucose = st.number_input("Glucose Level", value=0)

# Predict button
if st.button("Predict"):
    prediction = make_prediction(age, sex, cigsPerDay, totChol, sysBP, glucose)
    st.write("Prediction:", prediction)
