## Import des modules

from pkg_resources import Requirement
import streamlit as st

import plotly.express as px

import pandas as pd
## Utiliser toute l'eqpace disponible

st.set_page_config(layout='wide')

## Titre et organistaion du dashboard

st.title('Analyse de données marketing : comportement d’achat en ligne en fonction de l’âge et du statut marital')

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

##Regroupement des achats en ligne par âge 

NumWebPurchases_per_age = df2[['Age', 'NumWebPurchases']].groupby('Age', as_index=False).agg('sum').sort_values(by='NumWebPurchases', ascending=False)

with left_block:
    first_container = st.container()
    with first_container: 
        fig = px.bar(NumWebPurchases_per_age[:45], \
                    x='Age', \
                    y='NumWebPurchases', \
                    text='NumWebPurchases', \
                    title='Achats en ligne en fonction de l\'âge', \
                    labels={'NumWebPurchases': 'Achats en ligne', 'Age': 'Âge'},
                    color='Age',
                    color_continuous_scale='gray',
                    barmode='group')  
        fig.update_layout(plot_bgcolor='teal')
        fig.update_layout(width=1100,height=400)
        fig.update_layout(
        font_color='black',
        font_family='ylgn',
        font_size=15,
        title_font_color='rgb(44, 5, 50, 255)',
        title_font_size=25,
        title_font_family='balck',
        legend_title_font_color='red',
        legend_title_font_size=10,
        legend_title_font_family='black')
        st.plotly_chart(fig)

## Achats en ligne pendant la promotion en fonction du statut marital

number_purchase_discount = st.container()

with left_block:
    bouton_select = st.container()
    with bouton_select:
        bouton_marital_status = st.multiselect(
        label='Choisix du statut marital',
        options=df2['Marital_Status'].unique(),
        default=['Married', 'Together', 'Single', 'Divorced', 'Widow', 'Alone', 'Absurd', 'YOLO'])
    with number_purchase_discount: 
  
     web_purchase_per_marital_status = df2[['Marital_Status', 'NumDealsPurchases', 'NumWebPurchases']].groupby(by=['Marital_Status'], as_index=False).agg('count').sort_values(by='NumDealsPurchases', ascending=True)
     web_purchase_per_marital_status = web_purchase_per_marital_status.query('Marital_Status in @bouton_marital_status')
    
    fig2 = px.bar(web_purchase_per_marital_status,
    x="NumDealsPurchases",
    y="Marital_Status",
    color='NumWebPurchases',
    orientation='h',
    color_continuous_scale='Agsunset',
    title='Achats pendant la promotion en fonction du statut marital',
    labels={'NumDealsPurchases': 'Achats avec promotion', 'Marital_Status':'Statut marital'})
    fig2.update_layout(plot_bgcolor='teal')
    fig2.update_layout(width=1200,height=450)
    fig2.update_layout(
        font_color='black',
        font_family='Arial',
        font_size=10,
        title_font_color='rgb(44, 5, 50, 255)',
        title_font_size=15,
        title_font_family='Arial',
        legend_title_font_color='black',
        legend_title_font_size=15,
        legend_title_font_family='Arial')

    st.plotly_chart(fig2)

#Répartition par acceptation de la campagne des mariés

product_choice = df2[['Education','Response']].groupby(by=['Education'], as_index=False).count()

fig3 = px.pie(df2.query("Education == 'PhD'").round(),
values='Response',
names='Response',
title='Répartition de l\'acceptation et du refus de la campagne par les mariés',
color_discrete_sequence=px.colors.sequential.Agsunset
)
fig3.update_traces(textposition='inside', textinfo='percent+label')
fig2.update_layout(plot_bgcolor='white')
fig2.update_layout(width=700,height=500)
fig3.update_layout(
font_color='black',
font_family='Quicksand',
font_size=15,
title_font_color='rgb(44, 5, 148, 255)',
title_font_size=19,
title_font_family='Quicksand',
legend_title_font_color='red',
legend_title_font_size=15,
legend_title_font_family='Quicksand')
st.plotly_chart(fig3)























         






