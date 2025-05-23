import streamlit as st
import pandas as pd
import numpy as np

st.title("My Streamlit App")
st.header("_Streamlit_ is :blue[cool] :sunglasses:")

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.area_chart(chart_data)