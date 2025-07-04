#main stream app
import streamlit as st
from story_generator import generate_story, generate_title, continue_story
from utils import genre_emojis, apply_dark_mode, apply_genre_theme

st.set_page_config(page_title="AI Story Generator", layout="centered")

# Sidebar: Dark mode toggle
dark_mode = st.sidebar.checkbox("🌙 Enable Dark Mode")

# Title & prompt
st.title("🌟 Welcome to AI Story Generator!")

prompt = st.text_input("Enter a story idea or prompt", max_chars=200)
genre = st.selectbox("Choose a genre:", list(genre_emojis.keys()))
st.markdown(f"### Selected Genre: {genre_emojis[genre]} {genre}")

# Apply theme
if dark_mode:
    apply_dark_mode()
else:
    apply_genre_theme(genre)

# Length selection
length_option = st.selectbox("Choose story length:", ["Short", "Medium", "Long"])
length_map = {"Short": 150, "Medium": 300, "Long": 500}

# Session state
if 'full_story' not in st.session_state:
    st.session_state.full_story = ""

# Generate story
if st.button("✨ Generate Story"):
    if prompt.strip() == "":
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("Generating story..."):
            try:
                story = generate_story(prompt, genre, length_map[length_option])
                title = generate_title(prompt, genre)
                st.session_state.full_story = story

                st.subheader("📘 Story Title")
                st.success(title)

                st.subheader("📖 Story")
                st.write(story)

                rating = st.radio("⭐ Rate this story:", [1, 2, 3, 4, 5], index=2)

                file_name = f"{title.replace(' ', '_')}.txt"
                full_output = f"Genre: {genre}\nTitle: {title}\n\nStory:\n{story}\n\nRating: {rating}/5\n"
                st.download_button("⬇️ Download Story", full_output, file_name=file_name, mime="text/plain")

            except Exception as e:
                st.error(f"An error occurred: {e}")

# Continue story
if st.session_state.full_story:
    if st.button("➡️ Continue Story"):
        with st.spinner("Continuing story..."):
            try:
                continuation = continue_story(
                    st.session_state.full_story, genre, length_map[length_option] // 2
                )
                st.session_state.full_story += "\n\n" + continuation
                st.subheader("🧾 Continued Story")
                st.write(continuation)
            except Exception as e:
                st.error(f"Failed to continue story: {e}")
