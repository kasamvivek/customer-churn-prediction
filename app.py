import joblib
import streamlit as st

model = joblib.load("churn_model_small.pkl")
scaler = joblib.load("scaler_small.pkl")

st.title("📊 Churn Prediction Dashboard")

st.caption("Machine Learning based customer churn prediction system")

age = st.number_input("Enter Customer Age", min_value=18, max_value=100, value=30)

st.write("Customer Age:", age)

tenure = st.number_input("Enter Tenure in Months", min_value=0, max_value=100, value=12)

st.write("Tenure:", tenure)

monthly_charge = st.number_input(
    "Enter Monthly Charge",
    min_value=0.0,
    value=50.0
)

st.write("Monthly Charge:", monthly_charge)

satisfaction_score = st.number_input(
    "Enter Satisfaction Score",
    min_value=1,
    max_value=5,
    value=3
)

st.write("Satisfaction Score:", satisfaction_score)

number_of_referrals = st.number_input(
    "Enter Number of Referrals",
    min_value=0,
    value=0
)

st.write("Number of Referrals:", number_of_referrals)

if st.button("Predict Churn"):

    input_data = [[
        age,
        tenure,
        monthly_charge,
        satisfaction_score,
        number_of_referrals
    ]]

    input_data_scaled = scaler.transform(input_data)

    prediction = model.predict(input_data_scaled)

    probability = model.predict_proba(input_data_scaled)

    confidence = max(probability[0]) * 100

    if prediction[0] == 0:
        st.success("Customer Will Continue Service")
    else:
        st.error("Customer Is Likely To Churn")

    st.success(f"Model Confidence: {confidence:.2f}%")