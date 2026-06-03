import streamlit as st
import pandas as pd
import joblib

from src.nba import next_best_action
from src.ai_assistant import generate_brief
from src.relationship_manager import relationship_manager_brief

# Load model
model = joblib.load("models/churn_model.pkl")

# Page Config
st.set_page_config(
    page_title="AI Customer Retention & Personalization Platform",
    layout="wide"
)

# Sidebar
st.sidebar.title("Platform Capabilities")

st.sidebar.success("✓ Churn Prediction")
st.sidebar.success("✓ Customer Segmentation")
st.sidebar.success("✓ Next Best Action")
st.sidebar.success("✓ AI Relationship Manager Assistant")

# Main Title
st.title("AI-Powered Customer Retention & Personalization Platform")

st.markdown(
    """
This platform helps banks identify customers at risk of churn,
recommend personalized retention strategies,
and assist Relationship Managers with AI-generated customer insights.
"""
)

# Customer Inputs
st.header("Customer Profile")

col1, col2 = st.columns(2)

with col1:

    credit_score = st.slider(
        "Credit Score",
        300,
        900,
        650
    )

    age = st.slider(
        "Age",
        18,
        100,
        40
    )

    tenure = st.slider(
        "Tenure (Years)",
        0,
        10,
        5
    )

    balance = st.number_input(
        "Account Balance",
        value=50000.0
    )

    salary = st.number_input(
        "Estimated Salary",
        value=60000.0
    )

with col2:

    products = st.selectbox(
        "Number of Products",
        [1, 2, 3, 4]
    )

    credit_card = st.selectbox(
        "Has Credit Card",
        [0, 1]
    )

    active_member = st.selectbox(
        "Active Member",
        [0, 1]
    )

    geography_germany = st.selectbox(
        "Customer in Germany",
        [0, 1]
    )

    geography_spain = st.selectbox(
        "Customer in Spain",
        [0, 1]
    )

    gender_male = st.selectbox(
        "Male",
        [0, 1]
    )

# Prediction Button
if st.button("Predict Churn Risk"):

    # Build Input DataFrame
    data = pd.DataFrame([{
        "CreditScore": credit_score,
        "Age": age,
        "Tenure": tenure,
        "Balance": balance,
        "NumOfProducts": products,
        "HasCrCard": credit_card,
        "IsActiveMember": active_member,
        "EstimatedSalary": salary,
        "Geography_Germany": geography_germany,
        "Geography_Spain": geography_spain,
        "Gender_Male": gender_male
    }])

    # Predict Probability
    probability = model.predict_proba(data)[0][1]

    st.divider()

    # Churn Risk
    st.subheader("Customer Churn Risk")

    st.metric(
        "Predicted Churn Probability",
        f"{probability:.2%}"
    )

    # NBA Engine
    segment, action, reason = next_best_action(
        probability,
        balance,
        products,
        active_member
    )

    # Customer Segment
    st.subheader("Customer Segment")

    st.info(segment)

    # Next Best Action
    st.subheader("Next Best Action")

    st.success(action)

    st.write(reason)

    # Relationship Manager Brief
    st.subheader("Relationship Manager Brief")

    rm_brief = relationship_manager_brief(
        segment,
        probability,
        balance,
        products,
        active_member
    )

    st.text(rm_brief)

    # AI Context
    customer_context = f"""
    Customer Segment: {segment}

    Credit Score: {credit_score}
    Age: {age}
    Tenure: {tenure}

    Balance: {balance}
    Estimated Salary: {salary}

    Number of Products: {products}

    Active Member: {active_member}

    Churn Risk: {probability:.2%}

    Recommended Action: {action}

    Reason:
    {reason}
    """

    # AI Assistant
    st.subheader("AI Relationship Manager Assistant")

    with st.spinner("Generating customer insights..."):

        try:

            brief = generate_brief(
                customer_context
            )

            st.write(brief)

        except Exception as e:

            st.error(
                f"Unable to generate AI brief: {e}"
            )