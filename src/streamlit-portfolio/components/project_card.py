import streamlit as st

def project_card(title, description, link):
    card = f"""
    <div class="project-card">
        <h3>{title}</h3>
        <p>{description}</p>
        <a href="{link}" target="_blank">View Project</a>
    </div>
    """
    return st.markdown(card, unsafe_allow_html=True)