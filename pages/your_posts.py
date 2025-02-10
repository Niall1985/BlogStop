import streamlit as st
import json
import os
from footer import add_footer

post_db = "posts.json"
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
def load_posts():
    if os.path.exists(post_db):
        with open(post_db, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []

def save_posts(posts):
    with open(post_db, "w") as file:
        json.dump(posts, file, indent=3)

def delete_post(index):
    posts = load_posts()
    del posts[index]
    save_posts(posts)

def edit_post(index, new_title, new_content):
    posts = load_posts()
    posts[index]["Title"] = new_title
    posts[index]["Content"] = new_content
    save_posts(posts)

if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.error("⚠️ Please log in first.")
    st.stop()

st.title("📝 Your Posts") 
with st.sidebar:
    if st.button("🏠 Back to Home"):
        st.switch_page("pages/home.py")

username = st.session_state.username  
posts = load_posts()

user_posts = [post for post in posts if post["Name"] == username]

if not user_posts:
    st.info("No posts found. Create your first post! 🎉")
else:
    for index, post in enumerate(posts):
        if post["Name"] == username:
            st.subheader(post["Title"])
            st.write(post["Content"])
            
            with st.expander("✏️ Edit Post"):
                new_title = st.text_input(f"Edit Title {index}", value=post["Title"])
                new_content = st.text_area(f"Edit Content {index}", value=post["Content"], height=200)
                if st.button(f"💾 Save Changes {index}"):
                    edit_post(index, new_title, new_content)
                    st.success("✅ Post updated successfully!")
                    st.rerun()

            if st.button(f"🗑️ Delete Post"):
                delete_post(index)
                st.warning("❌ Post deleted!")
                st.rerun()

            st.markdown("---")

add_footer()