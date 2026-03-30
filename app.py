import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("best_model.pkl", "rb"))

st.title("Insomnia Detection")

age = st.slider("Age", 10, 80)
sleep_duration = st.slider("Sleep Duration", 0, 12)
stress_level = st.slider("Stress Level", 1, 10)
bmi = st.slider("BMI", 10, 40)
heart_rate = st.slider("Heart Rate", 50, 120)
steps = st.slider("Daily Steps", 0, 20000)

# Example for categorical
gender = st.selectbox("Gender", ["Male", "Female"])

# Convert categorical → numeric (IMPORTANT)
gender = 1 if gender == "Male" else 0

if st.button("Predict"):
    data = np.array([[age, gender, sleep_duration, stress_level, bmi, heart_rate, steps]])
    result = model.predict(data)
    st.write(result)
