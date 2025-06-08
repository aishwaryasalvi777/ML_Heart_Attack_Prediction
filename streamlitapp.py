import streamlit as st
import requests

# Set up the title and layout
st.set_page_config(
    page_title="FastAPI Frontend",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Add a header
st.title("🚀 FastAPI Frontend")

# Introduction text
st.markdown(
    """
    Welcome to the **FastAPI Frontend** built with Streamlit. 
    Enter your input, interact with the backend API, and see the results in real-time!
    """
)

# Add a sidebar for user settings or options
st.sidebar.header("Options")
api_url = st.sidebar.text_input(
    "API Base URL", "http://127.0.0.1:8000", help="Enter the base URL of your FastAPI backend"
)

# Input fields for the frontend
st.subheader("Input Parameters")
user_input = st.text_input("Enter some text:", "Hello FastAPI!")
numeric_input = st.number_input("Enter a number:", min_value=0, max_value=100, value=50)

# Button to trigger the API call
if st.button("Submit"):
    with st.spinner("Connecting to the API..."):
        try:
            # Sending data to the backend
            payload = {"text": user_input, "number": numeric_input}
            response = requests.post(f"{api_url}/process", json=payload)
            
            # Display the response
            if response.status_code == 200:
                st.success("API Response Received!")
                st.json(response.json())
            else:
                st.error(f"API Error: {response.status_code}")
        except requests.exceptions.RequestException as e:
            st.error(f"Connection Error: {e}")
