import streamlit as st
from streamlit_option_menu import option_menu
import json
import os
from footer import add_footer

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
            st.switch_page("pages/create_post.py")
        elif app == 'Your Posts':
            st.switch_page("pages/your_posts.py")
        elif app == 'Signout':
            signout()

def show_homepage():
    st.title("📢 Latest Posts")
    posts = load_posts()

    if posts:
        for post in reversed(posts): 
            st.subheader(post["Title"])
            st.subheader(post['Name'])
            st.write(post["Content"])
            st.markdown("---")
    else:
        st.info("No posts available. Create a new post to get started! 🎉")

def signout():

    for key in list(st.session_state.keys()):
        del st.session_state[key]
    
    st.switch_page("app.py")

app = MultiApp()
app.run()


add_footer()