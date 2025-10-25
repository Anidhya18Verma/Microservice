import streamlit as st
import random

# Initialize quotes (acts like backend)
if "quotes" not in st.session_state:
    st.session_state.quotes = [
        "The best way to predict the future is to invent it.",
        "Life is what happens when you're busy making other plans.",
        "You miss 100% of the shots you don’t take.",
        "In the middle of every difficulty lies opportunity.",
        "Do one thing every day that scares you."
    ]

# Streamlit Frontend
st.title("Random Quote Microservice")

# Sidebar for actions
action = st.sidebar.radio("Choose Action", ["Get Quote", "Add Quote"])

# Get Random Quote
if action == "Get Quote":
    if st.button("Get Random Quote"):
        quote = random.choice(st.session_state.quotes)
        st.success(quote)

# Add a New Quote
elif action == "Add Quote":
    new_quote = st.text_input("Enter a new quote")
    if st.button("Add Quote"):
        if new_quote.strip() == "":
            st.error("Quote cannot be empty!")
        else:
            st.session_state.quotes.append(new_quote.strip())
            st.success("Quote added successfully!")
