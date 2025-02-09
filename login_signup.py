import streamlit as st
import subprocess
import json
import os

st.set_page_config(page_title="SignUp/Login", layout="wide")
databse_file = "users.json"

def callhome():
    subprocess.run(["streamlit", "run","home.py"])

def load_users():
    if os.path.exists(databse_file):
        with open(databse_file, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return[]
    return[]

def save_user_data(email, username, password):
    user_data = {"email":email, "username": username, "password":password}

    if os.path.exists(databse_file):
        with open(databse_file, "r") as file:
            try:
                users = json.load(file)
            except json.JSONDecodeError:
                users = []
    else:
        users = []
    
    users.append(user_data)
    with open(databse_file, "w") as file:
        json.dump(users, file, indent=3)


def verify_user_login(username, password):
    users = load_users()
    for user in users:
        if user["username"] == username and user["password"] == password:
            return True
        return False

st.title("Welcome to :blue[BlogStop]!")

choice = st.selectbox(":blue[SignUp/Login]", ['SignUp', 'Login'])

if choice == 'SignUp':
    email = st.text_input('Enter your email id')
    username = st.text_input('Enter your username')
    password = st.text_input('Enter your password', type="password")
    confirm_password = st.text_input('Confirm your password', type="password")

    if confirm_password == password:
        if st.button(":green[Signup]"):  
            save_user_data(email, username, password)
            st.success("Signup successful! Redirecting to Home...")
            callhome()
    else:
        st.error("Passwords do not match. Please try again.")

else:
    username = st.text_input('Enter your username')
    password = st.text_input('Enter your password', type="password")
    if st.button(":green[Login]"):
        if verify_user_login(username, password):
            st.success("Logged in successfully!")
            callhome()  