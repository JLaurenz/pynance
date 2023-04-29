import streamlit as st
import plotly.graph_objects as go
import numpy as np

def main():
    st.set_page_config(page_title="PyNance")
    st.title("PyNance")
    st.header("Login")
    col1, col2 = st.columns(2)
    with col1:
        email = st.text_input("Enter your email: ")
    with col2:
        password = st.text_input("Enter your password: ", type="password")
    choice = st.radio("Login or Signup", ("Login", "Signup"))
    button = st.button(choice)

if button:
    if choice == "Login":
        try:
            auth.sign_in_with_email_and_password(email, password)
            st.success("Logged in as {}".format(email))
            st.balloons()
        except:
            st.error("Invalid email or password")
    elif choice == "Signup":
        try:
            auth.create_user_with_email_and_password(email, password)
            st.success("Successfully created account for {}".format(email))
        except:
            st.error("Email already exists")

if __name__ == "__main__":
    main()
