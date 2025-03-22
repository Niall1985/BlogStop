import streamlit as st
from streamlit_option_menu import option_menu
import json
import os
import webbrowser
from footer import add_footer
from dotenv import load_dotenv

load_dotenv()

portfolio = os.getenv("portfolio")

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

interaction_db = "interactions.json"

def load_interactions():
    if not os.path.exists(interaction_db):
        with open(interaction_db, "w", encoding="utf-8") as file:
            json.dump({}, file)  
    with open(interaction_db, "r", encoding="utf-8") as file:
        try:
            data = json.load(file)
            return data if isinstance(data, dict) else {}
        except json.JSONDecodeError:
            return {}

def save_interactions(data):
    with open(interaction_db, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

interactions = load_interactions()

menu = option_menu(
    menu_title="Pages",
    options=["🏡 Home", "➕ Create Post", "📧 Your Posts","📁 My Portfolio" ,"🔓 Sign Out"],
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
        "nav-link-selected": {"background-color": "blue", "color": "white"},
    }
)

if "page" not in st.session_state:
    st.session_state["page"] = "home"

if menu == "🏡 Home":
    st.session_state["page"] = "home"
elif menu == "➕ Create Post":
    st.switch_page("pages/create_post.py")
elif menu == "📧 Your Posts":
    st.switch_page("pages/your_posts.py")
elif menu == "📁 My Portfolio":
    webbrowser.open_new_tab(portfolio)
elif menu == "🔓 Sign Out":
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.switch_page("app.py")

post_db = "posts.json"

def load_posts():
    if not os.path.exists(post_db):
        with open(post_db, "w", encoding="utf-8") as file:
            json.dump([], file) 
    with open(post_db, "r", encoding="utf-8") as file:
        try:
            data = json.load(file)
            return data if isinstance(data, list) else []
        except json.JSONDecodeError:
            return []

posts = load_posts()

def show_homepage():
    st.title("📢 Latest Posts")

    username = st.session_state.get("username", "Anonymous")

    if posts: 
        for i, post in enumerate(reversed(posts)): 
            post_id = f"post_{i}"  
            
            if post_id not in interactions:
                interactions[post_id] = {"likes": 0, "comments": [], "liked_users": []}  # Ensure liked_users exists
         
            if "liked_users" not in interactions[post_id]:
                interactions[post_id]["liked_users"] = []

            with st.container():
                st.markdown(
                    f"""
                    <div style="background-color: rgb(41, 42, 54, 0.3); padding: 15px; border-radius: 10px; box-shadow: 2px 2px 10px rgba(0,0,0,0.1);">
                        <h3 style="color: white;">{post.get("Title", "Untitled Post")}</h3>
                        <p><strong>✍️ {post.get('Name', 'Unknown Author')}</strong></p>
                        <p>{post.get("Content", "No content available.")}</p>
                    </div>
                    """, 
                    unsafe_allow_html=True
                )
                st.markdown(f'''   ''')
             
                col1, col2 = st.columns([0.1, 0.1])
                
                with col1:
                    if username in interactions[post_id]["liked_users"]:
                        
                        if st.button(f"💔 {interactions[post_id]['likes']}", key=f"unlike_button_{i}"):
                            interactions[post_id]["likes"] -= 1  
                            interactions[post_id]["liked_users"].remove(username)  
                            save_interactions(interactions)
                            st.rerun()
                    else:
                
                        if st.button(f"❤️ {interactions[post_id]['likes']}", key=f"like_button_{i}"):
                            interactions[post_id]["likes"] += 1  
                            interactions[post_id]["liked_users"].append(username) 
                            save_interactions(interactions)
                            st.rerun()

                with col2:
                    if st.button("💬 Comment", key=f"comment_button_{i}"):
                        st.session_state[f"commenting_{post_id}"] = not st.session_state.get(f"commenting_{post_id}", False)

                if st.session_state.get(f"commenting_{post_id}", False):
                    comment = st.text_area("Leave a comment", key=f"comment_input_{i}")
                    if st.button("Submit Comment", key=f"submit_comment_{i}"):
                        if comment.strip():
                            interactions[post_id]["comments"].append({"user": username, "comment": comment})
                            save_interactions(interactions)
                            st.session_state[f"commenting_{post_id}"] = False 
                            st.rerun()

                if interactions[post_id]["comments"]:
                    st.markdown("### Comments:")
                    for c in interactions[post_id]["comments"]:
                        st.markdown(
                            f'''
                            <p style="
                                color: white; 
                                border: 1px solid white;
                                background-color: rgba(255, 255, 255, 0.1); 
                                padding: 8px; 
                                border-radius: 5px; 
                                margin: 5px 0;
                            ">
                            <strong>{c["user"]}</strong>: {c["comment"]}
                            </p>
                            ''',
                            unsafe_allow_html=True
                        )
    else:
        st.info("No posts available. Create a new post to get started! 🎉")

show_homepage()
add_footer()