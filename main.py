import streamlit as st
import plotly.graph_objects as go
import numpy as np
from log import db, auth

# set choice as global variable
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
                user = auth.sign_in_with_email_and_password(email, password)
                st.success("Logged in as {}".format(user["email"]))
            except:
                st.error("Invalid email or password")
    else:
        try:
            user = auth.create_user_with_email_and_password(email, password)
            st.success("Account created for {}".format(user["email"]))
        except:
            st.error("Account already exists")

if __name__ == "__main__":
    main()
