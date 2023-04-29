import streamlit as st
import plotly.graph_objects as go
import numpy as np
from log import db, auth, signup, login

# set choice as global variable
def main():
    st.set_page_config(page_title="PyNance")
    st.title("PyNance")
    # Login
    st.sidebar.title("Login")
    st.sidebar.subheader("Login to your account")
    # call log login function
    login()
    # Signup
    st.sidebar.title("Signup")
    st.sidebar.subheader("Create an account")
    # call log signup function
    signup()
    
if __name__ == "__main__":
    main()
