import streamlit as st
from modules import home, image_comprehension, grammar_fun, reading_translation

PAGES = {
    "🏠 Home": home,
    "🖼️ Image Comprehension": image_comprehension,
    "📘 Grammar & Fun": grammar_fun,
    "📖 Reading & Translation": reading_translation
}

PAGES1 = {"Home": [st.Page("config.py", title="Home")]}
st.set_page_config(page_title="Language Tutor", page_icon="🧠")
def main():
    st.sidebar.title('Navigation')
    pg = st.navigation(PAGES1,position="sidebar")
    pg.run()
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))
    st.set_page_config(initial_sidebar_state="collapsed")

    page = PAGES[selection]
    page.app()

if __name__ == "__main__":
    main()
