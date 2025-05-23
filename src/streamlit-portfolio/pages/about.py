import streamlit as st

def display_about():
    st.title("About Me")
    st.write("""
        Welcome to my portfolio! I am [Your Name], a passionate [Your Profession/Field].
        I specialize in [Your Specializations] and have a keen interest in [Your Interests].
        
        My journey in [Your Field/Industry] began [Brief Background or Story]. 
        Over the years, I have worked on various projects that have helped me grow and develop my skills.
        
        In this portfolio, you will find information about my projects, skills, and how to contact me.
        Thank you for visiting!
    """)

if __name__ == "__main__":
    display_about()