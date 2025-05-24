import streamlit as st
import pandas as pd
import numpy as np
from streamlit_timeline import timeline
import plotly.graph_objects as go

st.subheader('About me')
st.write(
    "This is a simple Streamlit app that demonstrates how to use Streamlit with Python. ")

st.subheader('Career snapshot')

with st.spinner(text="Building line"):
    with open('timeline.json', "r") as f:
        data = f.read()
        timeline(data, height=500)

st.subheader('Skills & Tools ⚒️')

# skills = list(['Data Science','RDBMS','Cassandra','AWS Athena','Snowflake','Comet-ML','Python','Java','C++','Airflow','AWS S3','Tableau','Metabase','Thoughtspot','Streamlit','PySpark','Tensorflow','Neo4j','Langchain','GenAI','AutoML'])
# skill_col_size = 5
# rows,cols = len(skills)//skill_col_size,skill_col_size
# if len(skills)%skill_col_size!=0:
#     print("Rows:", rows)

def skill_tab():
    skills = list(['Data Science','RDBMS','Cassandra','AWS Athena','Snowflake','Comet-ML','Python','Java','C++','Airflow','AWS S3','Tableau','Metabase','Thoughtspot','Streamlit','PySpark','Tensorflow','Neo4j','Langchain','GenAI','AutoML'])
    skill_col_size = 5
    rows,cols = len(skills)//skill_col_size,skill_col_size
    if len(skills)%skill_col_size!=0:
        rows+=1
    skills = iter(skills)
    for x in range(rows):
        columns = st.columns(skill_col_size)
        for index_ in range(skill_col_size):
            try:
                columns[index_].button(next(skills))
            except:
                break
with st.spinner(text="Loading section..."):
    skill_tab()

st.subheader('Education 📖')

degree = [['B.Tech','CSE','2020','IIIT Jabalpur','8.1 CGPA'],['12th','Science','2016','Bhavan\'s KDKVM', '94.2%'],['10th','-','2012','Bhavan\'s KDKVM','10 CGPA']]
edu = pd.DataFrame(degree,columns=['Qualification','Stream','Year','Institute','Score'])

fig = go.Figure(data=[go.Table(
    header=dict(values=list(edu.columns),
                fill_color='paleturquoise',
                align='left',height=65,font_size=20),
    cells=dict(values=edu.transpose().values.tolist(),
               fill_color='lavender',
               align='left',height=40,font_size=15))])

fig.update_layout(width=750, height=400)
st.plotly_chart(fig)