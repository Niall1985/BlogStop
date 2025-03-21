import streamlit as st
import json
import os
import bcrypt
from footer import add_footer
from encryption import encryption_func

def main():
    st.set_page_config(page_title="SignUp/Login", layout="wide")
    # st.sidebar.empty()
    st.markdown(
    """
    <style>
        [data-testid="stSidebarNav"], section[data-testid="stSidebar"] {
            display: none;
        }
    </style>
    """,
    unsafe_allow_html=True
)


    database_file = "users.json"

    def callhome():
        st.switch_page("pages/home.py")

    def load_users():
        if os.path.exists(database_file):
            with open(database_file, "r") as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    return []
        return []

    def save_user_data(email, username, password):
        user_data = {"email": email, "username": username, "password": password}

        if os.path.exists(database_file):
            with open(database_file, "r") as file:
                try:
                    users = json.load(file)
                except json.JSONDecodeError:
                    users = []
        else:
            users = []

        users.append(user_data)
        with open(database_file, "w") as file:
            json.dump(users, file, indent=3)

    def verify_user_login(username, password):
        users = load_users()
        for user in users:
            if user["username"] == username and user["password"] == password:
                return True
        return False


    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "username" not in st.session_state:
        st.session_state.username = None

    st.title("Welcome to :blue[BlogStop]!")

    if st.session_state.logged_in:
        st.success(f"Welcome, {st.session_state.username}! 🎉")
        callhome()
    
    else:
        choice = st.selectbox(":blue[SignUp/Login]", ['SignUp', 'Login'])

        if choice == 'SignUp':
            email = st.text_input('Enter your email id')
            username = st.text_input('Enter your username')
            password = st.text_input('Enter your password', type="password")
            confirm_password = st.text_input('Confirm your password', type="password")

            if confirm_password == password:
                if st.button(":green[Signup]"):
                    save_user_data(email, username, encryption_func(password))
                    st.success("Signup successful! Please log in.")
            else:
                st.error("Passwords do not match. Please try again.")

        else:  
            username = st.text_input('Enter your username')
            password = st.text_input('Enter your password', type="password")
            if st.button(":blue[Forgot Password]"):
                st.switch_page("pages/password_reset.py")
            
            if st.button(":green[Login]"):
                if verify_user_login(username, encryption_func(password)):
                    st.success(f"Logged in successfully! Welcome, {username} 🎉")
                    st.session_state.logged_in = True
                    st.session_state.username = username 
                    callhome()
                    st.rerun()  
                else:
                    st.error("Incorrect Username/Password entered")


    add_footer()

if __name__ == "__main__":
    main()