import pyrebase
import streamlit as st
import json

firebaseConfig = {
  'apiKey': "AIzaSyBj7haZR97aCD-gpDgdS71WZ3EctxGuS6o",
  'authDomain': "pynance-8f282.firebaseapp.com",
  'projectId': "pynance-8f282",
  'databaseURL': 'https://pynance-8f282-default-rtdb.firebaseio.com/',
  'storageBucket': "pynance-8f282.appspot.com",
  'messagingSenderId': "477676443144",
  'appId': "1:477676443144:web:c8da38d005e2715238e3bd",
  'measurementId': "G-QC5GTZ0KS8"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

db = firebase.database()
storage = firebase.storage()

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

