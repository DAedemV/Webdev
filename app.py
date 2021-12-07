from pkg_resources import Requirement
import streamlit as st

import plotly.express as px

import pandas as pd

Requirement
plotly==5.3
pandas==1.3
streamlit==1.1

st.set_page_config(layout='wide')

left_block, center_block, right_block = st.columns([2, 2, 2])

with left_block:
    st.write('# LEFT BLOCK')
    first_container = st. container()
    with first_container:
        st.header('Mon premier container')

with center_block:
    st.write('# CENTER BLOCK')
    st.header('Mon second container')

with right_block:
    st.write('# RIGHT BLOCK')
    st.header('Mon troisieme container')







