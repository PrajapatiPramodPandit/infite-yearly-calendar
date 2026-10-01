import streamlit as st

def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

st.markdown(
    '<div class="welcome-text">स्वागतम्</div>',
    unsafe_allow_html=True
)