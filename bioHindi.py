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
col1, col2= st.columns([2, 6])
with col1:
    st.markdown("<image style='margin-top: 20px;' src='https://raw.githubusercontent.com/PrajapatiPramodPandit/infite-yearly-calendar/refs/heads/main/asserts/IMG_20220818_161452_528.jpg' width=200px>",
       unsafe_allow_html=True
     )

with col1:
    st.markdown(
        "<p style='background-color: #FFF4DE;color: #000000;border-radius: 20px; padding: 10px;'>बाल बचन प्रसाद</p>",
        unsafe_allow_html=True
    )
with col2:
    st.markdown(
        "<p style='margin-top: 27px; background-color: #4C2365; padding: 10px;'>बाल बचन प्रसाद सेवा निर्वित प्रधानाध्यापक हैं। ये बिहार के सरकारी स्कूल में एक शिक्षक थे।"
          "ये लगभग 40 वर्षों तक शिक्षा के क्षेत्र में कार्यरत रहे हैं। इन्होंने कई सारे गणित के सूत्रों का विसित किया है। ये कैलंडर के लिए भी कई सारे सूत्रों का विसित किया है। ये कैलंडर आप देख सकते हैं। </p>"
        "</p>",
        unsafe_allow_html=True
    )