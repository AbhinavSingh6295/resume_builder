import streamlit as st
from components.header import header
from components.footer import footer
from pages import about, projects, skills, contact

def main():
    st.set_page_config(page_title="Portfolio", layout="wide")
    header()

    pages = {
        "About": about,
        "Projects": projects,
        "Skills": skills,
        "Contact": contact
    }

    selection = st.sidebar.selectbox("Navigate", list(pages.keys()))

    with st.spinner(f"Loading {selection} ..."):
        pages[selection].show()

    footer()

if __name__ == "__main__":
    main()