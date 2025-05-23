import streamlit as st
import json

# Load project data from JSON file
with open('data/projects.json') as f:
    projects = json.load(f)

st.title("Projects")

# Display each project
for project in projects:
    st.subheader(project['title'])
    st.write(project['description'])
    st.markdown(f"[View Project]({project['link']})")