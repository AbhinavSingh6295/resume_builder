import streamlit as st
import pandas as pd
import json

# Load skills data from JSON file
with open('data/skills.json') as f:
    skills_data = json.load(f)

# Title for the Skills page
st.title("Skills")

# Display skills
for skill in skills_data:
    st.subheader(skill['name'])
    st.progress(skill['proficiency'])  # Assuming proficiency is a value between 0 and 100
    st.write(skill['description'])