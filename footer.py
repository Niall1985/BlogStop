import streamlit as st

def add_footer():
    footer = """
    <style>
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: black;
            color: white;
            text-align: center;
            padding: 10px;
            font-size: 14px;
        }
    </style>
    <div class="footer">
        © 2024 BlogStop. All rights reserved.
    </div>
    """
    st.markdown(footer, unsafe_allow_html=True)
