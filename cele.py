import streamlit as st

# Define pages
hindi_page = st.Page(
    "hindi.py",
    title="Hindi",
    icon="🇮🇳"
)

english_page = st.Page(
    "English.py",
    title="English",
    icon="🇬🇧"
)

# Sidebar navigation
pg = st.navigation(
    {
        "🌐 Languages": [hindi_page, english_page]
    },
    position="sidebar"
)

# Run selected page
pg.run()