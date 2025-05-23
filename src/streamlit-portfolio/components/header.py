import streamlit as st

def header():
    st.title("My Portfolio")
    st.markdown("""
        <style>
            .nav-link {
                margin-right: 15px;
                text-decoration: none;
                color: #000;
            }
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <nav>
            <a class="nav-link" href="about">About</a>
            <a class="nav-link" href="projects">Projects</a>
            <a class="nav-link" href="skills">Skills</a>
            <a class="nav-link" href="contact">Contact</a>
        </nav>
    """, unsafe_allow_html=True)