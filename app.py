## Import des modules

from pkg_resources import Requirement
import streamlit as st

import plotly.express as px

import pandas as pd

## Utiliser toute l'eqpace disponible

st.set_page_config(layout='wide')

## Titre et organistaion du dashboard

st.title('Dashboard campaign marketing')

left_block, right_block = st.columns([1, 1])

## Import des données

# Chargement des données

mkt_camp = pd.read_csv('marketing_campaign')













         






