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


# When this method is called, it will create a new user in the database
def signup():
    st.subheader("Create New Account")
    new_email = st.text_input("Email")
    new_password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    if new_password == confirm_password:
        if st.button("Signup"):
            try:
                user = auth.create_user_with_email_and_password(new_email, new_password)
                st.success("You have successfully created a valid account")
                st.info("Go to Login Menu to login")
            except:
                st.error("Oops! Something went wrong...")
    else:
        st.warning("Passwords do not match")


# When this method is called, it will log the user in
def login():
    st.subheader("Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            st.success("You have successfully logged in")
            with open('user.json', 'w') as f:
                json.dump(user, f)
            st.info("Proceed to Prediction Menu")
        except:
            st.error("Oops! Something went wrong...")

