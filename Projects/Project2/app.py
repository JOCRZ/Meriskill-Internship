import streamlit as st
import numpy as np
import pandas as pd
import pickle



model=pickle.load(open('model.pkl','rb'))
st.title("Women Dibetes Prediction")
st.image("data//dib.jpg", width=500)


nav = st.sidebar.radio("Navigation",["Aim","Prediction"])      

if nav == 'Aim':
    st.markdown(""" #### Aim of the Project """)


def predict_buy(age):
    input=np.array([[age]]).astype(np.float64)

    prediction=model.predict(input)
    pred=prediction[0]
    return pred


if nav == 'Prediction':
    
    st.header('Probability to Buy Insurance')
    age = st.text_input("Age")
    glucose = st.text_input('Glucose Level')
    bmi = st.text_input('BMI value')
    ph = st.text_input('Pregnancy History ( How many times?)')
    dpf = st.text_input('')
    


    if st.button("Predict"):
        value = predict_buy(age)
        if value == 0:
            st.success('Not Buying Insurance')
        if value == 1:
            st.success('Buying Insurance')
    