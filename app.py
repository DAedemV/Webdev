## Import des modules

from pkg_resources import Requirement
import streamlit as st

import plotly.express as px

import pandas as pd
## Utiliser toute l'eqpace disponible

st.set_page_config(layout='wide')

## Titre et organistaion du dashboard

st.title('Analyse de données marketing : comportement d’achat en ligne en fonction du statut matrimonial et de l’âge')

left_block, right_block = st.columns([1, 1])

## Import des données

df = pd.read_csv('marketing_campaign.csv', sep=';')

# Création d'un nouveau JDD
df2 = df.copy() 
df2.reset_index(inplace=True)

#Calculer l'âge à partir de l'année de naissance
age = []
print (df2.info())
for i in df2['Year_Birth']:
    age.append(2021 - i)

df2['Age'] = age

#### PREMIER GRAPHIQUE ####

#Regroupement des achats en ligne par âge 

NumWebPurchases_per_age = df2[['Age', 'NumWebPurchases']].groupby('Age', as_index=False).agg('sum').sort_values(by='NumWebPurchases', ascending=False)
#st.write(NumWebPurchases_per_year_birth)

with left_block:
    st.subheader('Définition de la cible')
    first_container = st.container()
    with first_container: 
        fig = px.bar(NumWebPurchases_per_age[:50], \
                    x='Age', \
                    y='NumWebPurchases', \
                    text='NumWebPurchases', \
                    title='Nombre d\'achats en ligne en fonction de l\'âge', \
                    labels={'NumWebPurchases': 'Achats en ligne', 'Age': 'Âge'},
                    color='Age',
                    color_continuous_scale='Agsunset',
                    barmode='group')  
        fig.update_layout(plot_bgcolor='white')
        fig.update_layout(width=1300,height=500)
        fig.update_layout(
        font_color='black',
        font_family='Quicksand',
        font_size=15,
        title_font_color='rgb(44, 5, 148, 255)',
        title_font_size=25,
        title_font_family='Quicksand',
        legend_title_font_color='red',
        legend_title_font_size=15,
        legend_title_font_family='Quicksand')
        st.plotly_chart(fig)



















         






