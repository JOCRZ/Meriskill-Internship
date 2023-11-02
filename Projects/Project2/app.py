import streamlit as st
import numpy as np
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler




model=pickle.load(open('model.pkl','rb'))
st.title("Women Dibetes Prediction")
st.image("data//dib.jpg", width=500)


nav = st.sidebar.radio("Navigation",["Aim","Prediction"])      

if nav == 'Aim':
    st.markdown(""" #### Aim of the Project """)


def predict_buy(age,glucose,bmi,ph,dpf):
    input = np.array([[age,glucose,bmi,ph,dpf]]).astype(np.float64)
    prediction=model.predict(input)
    pred=prediction[0]
    return pred


if nav == 'Prediction':
    
    st.header('Probability to Buy Insurance')
    age = st.number_input("Age")
    glucose = st.slider('Glucose Level',min_value=30, max_value=1000, value=70)
    bmi = st.number_input('BMI value')
    ph = st.number_input('Pregnancy History ( How many times?)')
    dpf = st.number_input('Diabetes Pedigree Function')

    



    if st.button("Predict"):
        value = predict_buy(age,glucose,bmi,ph,dpf)
        if value == 0:
            st.success('Have Diabetes')
        if value == 1:
            st.success('Not Have Diabetes')
    