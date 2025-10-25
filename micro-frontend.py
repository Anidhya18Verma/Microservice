import streamlit as st
import requests

# Replace this with your Render public backend URL
API_URL = "https://my-flask-backend.onrender.com/quote"

st.title("Random Quote Microservice Frontend")

if st.button("Get a Random Quote"):
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            data = response.json()
            st.success(data["quote"])
        else:
            st.error("Failed to fetch quote from backend")
    except Exception as e:
        st.error(f"Error: {e}")
