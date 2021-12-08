from pkg_resources import Requirement
import streamlit as st

import plotly.express as px

import pandas as pd

st.set_page_config(layout='wide')

markt_campaign = pd.read_csv('marketing_campaign.csv')

markt_campaign.info()

st.title('Dashboard campagne marketing')

left_block, right_block = st.columns([1,1])

with left_block:
    with st.expander('Cliquer pour ouvrir les paramètres de recherche')
    st.write('# LEFT BLOCK')
    first_container = st. container()
    with first_container:
        st.header('Mon premier container')

with right_block:
    st.write('# RIGHT BLOCK')
    st.header('Mon troisieme container')







