import streamlit as st
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

with st.sidebar:
    if st.button("🏡 Home Page"):
        st.session_state["page"] = "home"
    if st.button("➕ Create Post"):
        st.switch_page("pages/create_post.py")
    if st.button("📧 Your Posts"):
        st.switch_page("pages/your_posts.py")
    if st.button("🔓 Sign Out"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.switch_page("app.py")

def show_homepage():
    st.title("📢 Latest Posts")
    posts = load_posts()

    if posts:
        for post in reversed(posts): 
            with st.container():
                st.subheader(post["Title"])
                st.write(f"✍️ {post['Name']}")
                st.write(post["Content"])
                st.markdown("---")
    else:
        st.info("No posts available. Create a new post to get started! 🎉")

show_homepage()

add_footer()
