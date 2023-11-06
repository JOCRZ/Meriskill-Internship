import streamlit as st
import numpy as np
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler


df = pd.read_csv('diabetes.csv')
model=pickle.load(open('model2.pkl','rb'))
st.image("data//dib.jpg", width=700)


nav = st.sidebar.radio("Navigation",["About","Prediction","Dashboard"])      

if nav == 'About':
    st.markdown(""" #### What is Gestational Diabetes? """)
    st.markdown(""" Gestational diabetes is a form of diabetes that occurs during pregnancy, affecting about 1 in 10 pregnant women. Unlike type 1 and type 2 diabetes, it's primarily caused by pregnancy-related physiological changes that lead to insulin resistance, hindering the normal delivery of glucose for energy in the body.""")
    st.markdown("""The Aim of a Gestational diabetes predictive model is to identify pregnant women at risk of developing diabetes during pregnancy so that preventive measures and early intervention can be applied to ensure better maternal and fetal health.""")

if nav == 'Dashboard':
    st.title('Model Dashboard')

    st.markdown("""Model used Random Forest Classifier""")
    kpi1,kpi2,kpi3,kpi4 = st.columns(4)
    kpi1.metric(label= "Total Patients" ,value= df.shape[0])
    kpi2.metric(label= "Total Dibetic Patients" ,value= len(df[df['Outcome'] == 1]))
    kpi3.metric(label= "Total Non-Dibetic Patients" ,value= len(df[df['Outcome'] != 1]))
    kpi4.metric(label="Mean Accuracy",value=0.766)
       

def predict_buy(age,glucose,bmi,ph,dpf):
    input = np.array([[age,glucose,bmi,ph,dpf]]).astype(np.float64)
    prediction=model.predict(input)
    pred=prediction[0]
    return pred


if nav == 'Prediction':
    
    st.header('Are you Risk of Developing Diabetes ?')
    st.markdown("""Please ensure to fill all the required fields.""")
    age = st.text_input("Age")
    glucose = st.slider('Glucose Level',min_value=30, max_value=1000, value=70)
    bmi = st.text_input('BMI value')
    ph = st.text_input('Pregnancy History ( How many times?)')
    dpf = st.text_input('Diabetes Pedigree Function')

    



    if st.button("Predict"):
        value = predict_buy(age,glucose,bmi,ph,dpf)
        if value == 0:
            st.success('No Risk of Diabetes')
            st.text("Wishing you a healthy delivery ahead")
        if value == 1:
            st.success('Risk of Diabetes')
            st.text("Remember, you're strong, and you've got this.")
    

   