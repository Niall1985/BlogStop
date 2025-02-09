import streamlit as st
from streamlit_option_menu import option_menu
import json
import os
import subprocess

st.title("Welcome to the :blue[Home Page]")

post_db = "posts.json"
def load_posts():
    if os.path.exists(post_db):
        with open(post_db, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, function):
        self.apps.append({"title": title, "function": function})

    def run(self): 
        with st.sidebar:
            app = option_menu(
                menu_title="Navigation",
                options=['Home', 'Your Posts', 'Create Post', 'Signout'],
                icons=['house-fill', 'file-text-fill', 'plus-circle-fill', 'box-arrow-right'],
                menu_icon='menu-button-wide',
                default_index=0,
                styles={
                    "container": {"padding": "5px", "background-color": "black"},
                    "icon": {"color": "white", "font-size": "23px"},
                    "nav-link": {"color": "white", "font-size": "20px", "text-align": "center"},
                    "nav-link-selected": {"background-color": "#02ab21"},
                }
            )

        if app == 'Home':
            show_homepage()
        elif app == 'Create Post':
              subprocess.Popen(["streamlit", "run", "create_post.py"], start_new_session=True)
        elif app == 'Signout':
              subprocess.Popen(["streamlit", "run", "login_signup.py"], start_new_session=True) 


def show_homepage():
    st.title("📢 Latest Posts")
    posts = load_posts()

    if posts:
        for post in reversed(posts):  # Show latest posts first
            st.subheader(post["Title"])
            st.write(post["Content"])
            st.markdown("---")
    else:
        st.info("No posts available. Create a new post to get started! 🎉")

app = MultiApp()
app.run()
