import streamlit as st
import numpy as np
from sklearn.preprocessing import StandardScaler
import joblib

st.set_page_config(layout="wide")
scaler = joblib.load("Scaler.pkl")

st.title("Dine Rank")


st.caption("This app helps you to predict a restaurant review class from India")

st.divider()

averagecost = st.number_input(
    "Please enter the estimated average cost for two person serving", min_value=50, max_value=99999999, step=200)

tablebooking = st.selectbox("Restaurant has table booking?", ["Yes", "No"])

onlinedelivery = st.selectbox("Restaurant has online booking?", ["Yes", "No"])

pricerange = st.selectbox(
    "What is the price range (1 Cheapest, 4 Most Expensive)", [1, 2, 3, 4])

predictbutton = st.button("Predict the review!")

st.divider()

model = joblib.load("mlmodel.pkl")

bookingstatus = 1 if tablebooking == "Yes" else 0

deliverystatus = 1 if onlinedelivery == "Yes" else 0

values = [[averagecost, bookingstatus, deliverystatus, pricerange]]
my_X_values = np.array(values)

X = scaler.transform(my_X_values)

if predictbutton:
    st.snow()
    prediction = model.predict(X)

    # Above 2 below 2.5 Poor
    # Above 2.5 below 3.5 Average
    # Above 3.5 below 4.0 Good
    # Above 4.0 below 4.5 Very Good
    # Above 4.5 Excellent

    if prediction < 2.5:
        st.write("Poor")
    elif prediction < 3.5:
        st.write("Average")
    elif prediction < 4.0:
        st.write("Good")
    elif prediction < 4.5:
        st.write("Very Good")
    else:
        st.write("Excellent")