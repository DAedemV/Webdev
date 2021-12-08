from pkg_resources import Requirement
import streamlit as st

import plotly.express as px

import pandas as pd

st.set_page_config(layout='wide')

marketing_campaign = pd.read_csv('C:/Users/53734R/OneDrive - MAIF/Bureau/Webdev/marketing_campaign.csv')

left_block, center_block, right_block = st.columns([2, 2, 2])

with left_block:
    st.write('# LEFT BLOCK')
    first_container = st. container()
    with first_container:
        st.header('Mon premier container')

with center_block:
    st.write('# CENTER BLOCK')
    st.header('Ton second container')

with right_block:
    st.write('# RIGHT BLOCK')
    st.header('Mon troisieme container')







