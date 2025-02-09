import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
import json

load_dotenv()
key = os.getenv('key')
genai.configure(api_key=key)

post_db = 'posts.json'

def save_posts(post_title, post_content):
    post_data = {"Title": post_title, "Content": post_content}

    if os.path.exists(post_db):
        with open(post_db, "r") as file:
            try:
                posts = json.load(file)
            except json.JSONDecodeError:
                posts = []
    else:
        posts = []

    posts.append(post_data)
    with open(post_db, "w") as file:
        json.dump(posts, file, indent=3)

st.title("Create your :blue[Post]!")

if "ai_content" not in st.session_state:
    st.session_state.ai_content = ""

post_title = st.text_input('Post Title')

post_content = st.text_area('Post Content', value=st.session_state.ai_content, height=300)

if st.button('Publish Post'):
    if post_title and post_content:
        save_posts(post_title, post_content)
        st.success("✅ Your post has been published!")
        st.session_state.ai_content = ""  # Reset AI content after publishing
    else:
        st.warning("⚠️ Please enter a title and content before publishing.")

if st.button('Write with AI'):
    if not post_title:
        st.warning("⚠️ Please enter a post title before using AI.")
    else:
        st.info("✨ Generating content using AI...")

        prompt = f"Write a blog post titled '{post_title}'. Keep it engaging and informative."

        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)

        if response and response.text:
            st.session_state.ai_content = response.text  # Update AI content in session state
            st.rerun()  # Refresh the app to update the text area
        else:
            st.error("❌ Failed to generate content. Please try again.")
