import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from PIL import Image



st.title('Real estate AI assistant')
st.markdown('The purpose of this app is to summarise and analyse real estate data of plots in Zambia')
st.divider()  # 👈 Draws a horizontal rule

image = Image.open('real.jpg')

st.image(image, caption='AI in Real Estate')

DATA_URL = ('area.xlsx')
# Create a text element and let the reader know the data is loading.

menu = st.sidebar.radio("Menu",['Home', 'Analysis'])
@st.cache_data
def load_data(nrows):
    data = pd.read_excel(DATA_URL)
    data.round(2)
    return data


if menu =='Home':
# Load 10,000 rows of data into the dataframe.
    data = load_data(5)
    # Notify the reader that the data was successfully loaded.
   
    st.markdown('## Metrics')
    st.text('The highest price per square metre is Ibex Hill, Lusaka')
    st.text('The lowest price is Shimabala, Chilanga.')
    mean = "K{:,}".format(data['price_square_metres'].mean().__round__(2), help='Average price per square meter')
    min = "K{:,}".format(data['price_square_metres'].min().__round__(2), help='Minimum price per square meter')
    max = "K{:,}".format(data['price_square_metres'].max().__round__(2), help='Maximum price per square meter')
    median = "K{:,}".format(data['price_square_metres'].median().__round__(2), help='Median price per square meter')

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Average price PSQM", mean)
    col2.metric("Lowest price PSQM", min )
    col3.metric("highest price PSQM", max )
    col4.metric("median price PSQM", median )
    

else:
    data = load_data(5)
    # Notify the reader that the data was successfully loaded.
    
    
    st.markdown('## Charts')
    st.text('Chart below is price per square meter in Zambian Kwacha')

    fig = px.histogram(data, x="price_square_metres", title='Price Per Square Meter')
    st.plotly_chart(fig,use_container_width=True)
    st.divider()  # 👈 Draws a horizontal rule


    fig = px.histogram(data, x="square_metres", title='Square meters')
    st.plotly_chart(fig,use_container_width=True)
    st.divider()  # 👈 Draws a horizontal rule
    st.text('The most sold property size of plot according to square meters is below 4900 SQM')
    st.text('4900 square meters turns out to be 70*70')
    st.divider()  # 👈 Draws a horizontal rule

    fig = px.box(data, x="price", title='Price of Plot')
    st.plotly_chart(fig,use_container_width=True)
    st.divider()  # 👈 Draws a horizontal rule

    st.text('With a median of K65,000 price for plots listed around the country.')
    st.text('The mean price of 600SQM, (20*30) is ZMW 113K')
    st.divider()  # 👈 Draws a horizontal rule

