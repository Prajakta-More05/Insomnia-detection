import streamlit as st
import pickle
import numpy as np

st.title("😴 Insomnia Detection System")

# Load model
try:
    model = pickle.load(open("best_model.pkl", "rb"))
    st.success("Model loaded successfully!")
except Exception as e:
    st.error(f"Error loading model: {e}")

# Inputs
age = st.slider("Age", 10, 80)
sleep_duration = st.slider("Sleep Duration", 0, 12)
stress_level = st.slider("Stress Level", 1, 10)

# Prediction
if st.button("Predict"):
    try:
        data = np.array([[age, sleep_duration, stress_level]])
        result = model.predict(data)

        if result[0] == 1:
            st.error("High Insomnia Risk")
        else:
            st.success("Normal Sleep")

    except Exception as e:
        st.error(f"Prediction error: {e}")
