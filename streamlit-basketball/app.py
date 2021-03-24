import streamlit as st
import pandas as pd
import base64
import numpy as np
import plotly.express as px

'''
# NBA Player Stats Explorer
Made with **streamlite** by _riztekur_
'''

st.sidebar.header('User Input Features')
year = st.sidebar.selectbox('Year', list(reversed(range(1950,2022))))

st.sidebar.multiselect('Team')

st.sidebar.multiselect('Position')

@st.cache
def load_data(year):
    url = "https://www.basketball-reference.com/leagues/NBA"