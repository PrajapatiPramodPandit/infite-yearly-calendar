import streamlit as st

# load CSS file----------------------------------------------------------
def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# Welcome text and description-------------------------------------------
st.markdown(
    '<div class="welcome-text">स्वागतम्</div>',
    unsafe_allow_html=True
)
st.markdown(
    '<div class="d1">'
    '<h6>यह कैलेंडर किसी भी तिथियों के दिनों को दिखाता है|</h6>'
    '</div>',
    unsafe_allow_html=True  
)

st.markdown(
    '<div class="d2">'

    '</div>',
    unsafe_allow_html=True  
)
st.markdown(
    '<div class="d3">'
    
    '</div>',
    unsafe_allow_html=True  
)
st.markdown(
    '<div class="d4">'
    
    '</div>',
    unsafe_allow_html=True  
)

if st.button("सोधकर्ता के बारे में", key="red_button"):
    st.switch_page("bioHindi.py")
