import streamlit as st

# Hardcoded username and password (for demonstration purposes)
valid_username = "user"
valid_password = "password"

# Streamlit app
st.title("Login Page")

# Input fields for username and password
username = st.text_input("Username")
password = st.text_input("Password", type="password")

# Login button
if st.button("Login"):
    # Check if the entered username and password are valid
    if username == valid_username and password == valid_password:
        st.success("Login successful!")
        # Add further logic for the authenticated user
    else:
        st.error("Invalid username or password. Please try again.")
