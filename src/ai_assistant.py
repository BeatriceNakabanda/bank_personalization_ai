import streamlit as st
from openai import OpenAI

client = OpenAI(
    api_key=st.secrets["OPENAI_API_KEY"]
)

def generate_brief(customer_data):

    prompt = f"""
    You are a senior banking relationship manager.

    Customer Profile:

    {customer_data}

    Generate:

    1. Customer Summary
    2. Risks
    3. Opportunities
    4. Suggested Conversation Strategy
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )

    return response.choices[0].message.content
