#themes
import streamlit as st

genre_emojis = {
    "Fantasy": "🧝‍♂️",
    "Sci-Fi": "🚀",
    "Horror": "👻",
    "Mystery": "🕵️‍♀️",
    "Romance": "💘"
}

genre_colors = {
    "Fantasy": "#f3e8ff",   # Soft lavender
    "Sci-Fi": "#e0f7ff",    # Pale sky blue
    "Horror": "#1f1f1f",    # Deep gray
    "Mystery": "#fffbe6",   # Pale yellow
    "Romance": "#ffe6f0"    # Gentle pink
}

def apply_dark_mode():
    st.markdown("""
        <style>
            .stApp {
                background-color: #1e1e1e;
                color: white;
            }
        </style>
    """, unsafe_allow_html=True)

def apply_genre_theme(genre):
    color = genre_colors.get(genre, "#ffffff")
    st.markdown(f"""
        <style>
            .stApp {{
                background-color: {color};
            }}
        </style>
    """, unsafe_allow_html=True)
