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
df = pd.read_excel('marketing_campaign.xls', sheet_name='marketing_campaign')

#Transformer les données
del df['Complain']
#st.dataframe(df)

# Création d'un nouveau JDD
df2 = df.copy() 
df2.reset_index(inplace=True)
#st.dataframe(df2)

#Calculer l'âge à partir de l'année de naissance
age = []
for i in df2['Year_Birth']:
    age.append(2021 - i)

df2['Age'] = age












         






