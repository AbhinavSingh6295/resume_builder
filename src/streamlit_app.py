import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title='mehul gupta\'s portfolio' ,layout="wide",page_icon='👨‍🔬')

st.sidebar.markdown(info['Stackoverflow_flair'],unsafe_allow_html=True)

st.title("My Streamlit App")
st.header("_Streamlit_ is :blue[cool] :sunglasses:")

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.area_chart(chart_data)

