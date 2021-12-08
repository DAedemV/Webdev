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

with st.expander('Cliquez pour ouvrir les paramètres de recherche'):
    st.write("""
             Choisissez ci-dessous les paramètres adaptés pour
             filtrer les données représentées sous forme de graphiques:
    """)

    dates = marketing_campaign['order_date']
    categories = marketing_campaign['Category'].unique()
    segments = marketing_campaign['Segment'].unique()
    regions = marketing_campaign['Region'].unique()

    date_range = st.slider('Sélectionnez l\'intervalle de temps considéré :',
        min_value=dates.min(),
        value=(dates.min().to_pydatetime(), dates.max().to_pydatetime()),
        max_value=dates.max(),
        format='DD/MM/YY'
    )
    start_date, end_date = date_range

    selected_categories = st.multiselect(
        label = 'Sélectionnez les catégories de produit :',
        options = categories,
        default = categories
    )

    selected_segments = st.multiselect(
        label = 'Sélectionnez les types de clientèle :',
        options = segments,
        default = segments
    )

    selected_regions = st.multiselect(
        label = 'Sélectionnez les régions :',
        options = regions,
        default = regions
    )

    marketing_campaign = marketing_campaign.query('order_date >= @start_date \
        and order_date <= @end_date \
        and Category in @selected_categories \
        and Segment in @selected_segments \
        and Region in @selected_regions \
    ')

    if marketing_campaign.empty:
        st.error('Pas de données pour cette sélection : choisissez d\'autres paramètres.')
        st.stop()

with left_block:
    st.subheader('Quantité de produits vendus')
    products_sold_per_category_container = st.container()
    with products_sold_per_category_container:
        
        fig1 = px.pie(marketing_campaign, values='Quantity', names='Category', title='Nombre de produits vendus par catégorie')
        st.plotly_chart(fig1, use_container_width=True, config={'displayModeBar': False})

    products_per_city_container = st.container()
    with products_per_city_container:
        products_per_city = marketing_campaign[['City', 'Region', 'Quantity']].groupby(['City', 'Region']) \
            .agg('sum') \
            .sort_values(by='Quantity', ascending=False)
        products_per_city.reset_index(inplace=True)

        fig2 = px.bar(products_per_city[:10], \
             x='Quantity', \
             y='City', \
             text='Quantity', \
             title='TOP 10 : Nombre de produits vendus par Ville', \
             orientation='h')
        # Petit hack (Voir https://plotly.com/python/axes/)
        fig2.update_yaxes(autorange='reversed')


with right_block:
    st.subheader('Ventes et Profits')

    sales_per_day_and_region_container = st.container()
    with sales_per_day_and_region_container:
        fig3 = px.scatter(marketing_campaign,x='Sales', y='Profit', size='Quantity', color='Region', hover_data=['Product Name', 'Order ID'])
        st.plotly_chart(fig3, use_container_width=True, config={'displayModeBar': False})
    
    shipping_mode_profits_container = st.container()
    with shipping_mode_profits_container:
        traductions={'Sales': 'Nombre de ventes (en $)', \
             'Region': 'Région des USA', \
             'Profit' : 'Profits (en $)', \
             'Ship Mode': 'Mode de livraison'}

        fig4 = px.density_heatmap(marketing_campaign, \
            x='Sales', \
            y='Region', \
            z='Profit', \
            histfunc='avg', \
            nbinsx=4, \
            nbinsy=4, \
            facet_col='Ship Mode', \
            labels=traductions, \
            title='Quelle est la configuration la plus rentable ?')
        fig4.update_layout(font_size=10, title_font_size=18) # Paramètres à découvrir dans la documentation !
        st.plotly_chart(fig4, use_container_width=True, config={'displayModeBar': False})

         






