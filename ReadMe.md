# Personalized Banking Intelligence Platform

An AI-powered customer retention and personalization platform designed to help financial institutions identify customers at risk of churn, recommend personalized interventions, and support Relationship Managers with intelligent customer insights.

The platform combines Machine Learning, customer segmentation, Next Best Action (NBA) recommendations, and Generative AI to improve customer engagement, retention, and product adoption.

## Live Demo

🚀 Try the application here:

**https://bankpersonalizationai-1.streamlit.app/**

## Business Problem

Banks continuously face challenges in:

- Customer churn and attrition
- Low product adoption
- Limited personalization at scale
- Inconsistent customer engagement
- Lack of actionable customer insights

This platform demonstrates how Machine Learning and AI can be used to proactively identify at-risk customers and enable personalized customer conversations.

## Solution Overview

The platform provides four key capabilities:

### 1. Customer Churn Prediction

A Random Forest Machine Learning model predicts the likelihood of a customer leaving the bank based on:

- Credit score
- Age
- Account tenure
- Account balance
- Product holdings
- Customer activity
- Geographic information
- Salary information

The model outputs a churn probability score for each customer.


### 2. Customer Segmentation

Customers are automatically segmented based on churn risk and customer value.

Example segments include:

- High Value At Risk
- Growth Opportunity
- Loyal Customer
- Stable Customer

These segments help prioritize customer engagement strategies.


### 3. Next Best Action Engine

The platform recommends personalized retention and growth actions such as:

- Relationship Manager outreach
- Product cross-selling
- Loyalty retention campaigns
- Premium banking offers
- Customer engagement initiatives

Recommendations are generated using customer risk and profile characteristics.

### 4. AI Relationship Manager Assistant

A Generative AI assistant produces customer-specific engagement briefs that help Relationship Managers:

- Understand customer risk factors
- Prepare personalized conversations
- Identify retention opportunities
- Recommend relevant banking products
- Improve customer experience


## Machine Learning Pipeline

### Data Preparation

- Missing value handling
- Feature engineering
- One-hot encoding
- Dataset cleaning

### Model Training

- Random Forest Classifier
- Train/Test Split
- Model Evaluation

### Model Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

### Model Explainability

- Feature Importance Analysis
- SHAP Explainability


## Technology Stack

### Data Science

- Python
- Pandas
- NumPy
- Scikit-learn

### AI

- OpenAI API
- Generative AI

### Visualization

- Matplotlib
- Seaborn

### Deployment

- Streamlit

### Model Persistence

- Joblib

### Version Control

- Git
- GitHub


## Business Impact

This platform demonstrates how banks can:

- Reduce customer churn
- Improve customer retention
- Increase product adoption
- Personalize customer interactions
- Support Relationship Managers with AI
- Drive data-driven decision making


## Future Enhancements

- Real-time customer scoring
- Recommendation systems
- Customer lifetime value prediction
- Marketing campaign optimization
- A/B testing framework
- Cloud deployment on Azure/AWS
- MLOps monitoring pipeline
- Customer 360 analytics


## Author

Beatrice Nakabanda

Data Scientist | Machine Learning Engineer | Software Engineer

Focused on building AI-powered solutions that solve real business problems through data, machine learning, and intelligent systems.