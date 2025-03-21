import streamlit as st
from streamlit_option_menu import option_menu
import json
import os
from footer import add_footer

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
st.title("Welcome to :blue[Blog]Stop!")
# menu = option_menu(
#     menu_title = "Pages",
#     options = ["🏡 Home Page", "➕ Create Post", "📧 Your Posts", "🔓 Sign Out"],
#     default_index=0,
#     orientation="horizontal",
# )

menu= option_menu(
    menu_title="Pages",
    options=["🏡 Home", "➕ Create Post", "📧 Your Posts", "🔓 Sign Out"],
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"background-color": "rgba(0,0,0,0)", "padding": "5px"},
        "icon": {"color": "white", "font-size": "18px"},
        "nav-link": {
            "color": "blue",
            "font-size": "16px",
            "text-align": "center",
            "margin": "0px",
            "--hover-color": "#d2d9d7",
        },
        "nav-link-selected": {"background-color": "#9E1A1A", "color": "white"},
    }
)

if menu == "🏡 Home Page":
    st.session_state["page"] = "home"
elif menu == "➕ Create Post":
    st.switch_page("pages/create_post.py")
elif menu == "📧 Your Posts":
    st.switch_page("pages/your_posts.py")
elif menu == "🔓 Sign Out":
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.switch_page("app.py")

post_db = "posts.json"

def load_posts():
    if os.path.exists(post_db):
        with open(post_db, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []

# Show Homepage Content
if st.session_state.get("page") == "home":
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

# Add Footer
add_footer()
