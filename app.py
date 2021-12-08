from pkg_resources import Requirement
import streamlit as st

import plotly.express as px

import pandas as pd

st.set_page_config(layout='wide')


def load_data():
    return pd.read_csv('marketing_campaign.csv', parse_dates=['Order Date', 'Ship Date'])

marketing_campaign = load_data()
marketing_campaign.rename(
    columns={
        'Order Date': 'order_date',
        'Ship Date': 'ship_date'
    },
    inplace = True
)

st.title('Dashboard campagne marketing')

left_block, right_block = st.columns([1, 1])


         






