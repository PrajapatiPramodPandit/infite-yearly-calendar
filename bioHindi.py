import streamlit as st

#load css file-----------------------------------------------------------
def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

#edit page title and icon-----------------------------------------------------------
st.markdown(
    '<h1>आपका स्वागत है।</h1>',
    unsafe_allow_html=True
)
#lading image-----------------------------------------------------------
col1, col2, col3 = st.columns([1, 6, 1])
with col1:
    st.markdown("<image src='' width=100 height=100>",
       unsafe_allow_html=True
     )