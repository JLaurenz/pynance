import pyrebase
import json
import streamlit as st

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

choice = st.sidebar.selectbox("Menu", ["Login", "Signup"])

email = st.sidebar.text_input("Email")
password = st.sidebar.text_input("Password", type='password')