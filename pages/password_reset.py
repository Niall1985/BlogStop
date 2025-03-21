import streamlit as st
import json
import os
from footer import add_footer
from encryption import encryption_func

database_file = "users.json"
st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                display: none;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
def load_users():
    if os.path.exists(database_file):
        with open(database_file, "r") as file:
            try:
                return json.load(file)  
            except json.JSONDecodeError:
                return []  
    return []

def save_users(users):
    with open(database_file, "w") as file:
        json.dump(users, file, indent=3)

def update_password(username, new_password):
    users = load_users()
    for user in users:
        if user["username"] == username:
            user["password"] = new_password  
            save_users(users)  
            return True    

st.title("Change your :blue[Password]")

username = st.text_input("Enter your existing username")
new_password = st.text_input("Enter your new password", type="password")
confirm_new_password = st.text_input("Confirm your password", type="password")

success = False

if st.button(":green[Update Password]"):
    if new_password == confirm_new_password:
        success = update_password(username, encryption_func(new_password))
        if success:
            st.success("Password updated successfully!")
            st.switch_page("pages/temp.py")
        else:
            st.error("User not found. Please check your username.")
    else:
        st.error("Passwords do not match. Please try again.")

add_footer()