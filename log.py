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
# with the given email and password
def signup(email, password):
    try:
        user = auth.create_user_with_email_and_password(email, password)
        return user
    except:
        return None