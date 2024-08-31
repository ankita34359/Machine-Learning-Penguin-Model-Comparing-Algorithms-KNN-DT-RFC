import streamlit as st
import joblib 
import numpy as np
import pandas as pd

st.header("Penguin")

CulmenLength = st.number_input("Enter Culmen Length in millimeters(mm)")
CulmenDepth = st.number_input("Enter Culmen Depth in millimeters(mm)")
FlipperLength = st.number_input("Enter Flipper Length in millimeters(mm)")
BodyMass = st.number_input("Enter Body Mass in grams (g)")

button = st.button("Submit")

loaded_model = joblib.load(r"C:\Users\Lenovo\OneDrive\Desktop\Juypter_projects\penguin_model.pkl")
# loaded_model = joblib.load(penguin_model_pkl)

X = np.array([[CulmenLength,CulmenDepth ,FlipperLength ,BodyMass ]])

predicted_value = loaded_model.predict(X)

decode_dict = {0:"Adelie", 1:"Chinstrap", 2:"Gentoo"}

predicted_name = decode_dict[predicted_value[0]]

if button:
    st.info(predicted_value)
    st.info(predicted_name)