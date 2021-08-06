import streamlit as st
import deku_methods as dm
import pyEX as p
import config
import pandas
from functools import wraps
from io import BytesIO
import pandas as pd
import requests
from deprecation import deprecated
from IPython.display import Image as ImageI
from PIL import Image as ImageP
from sqlalchemy import create_engine


print("Initializing gui...")

symbol = st.sidebar.text_input("Symbol", value='GME')


# stock = IEXStock(config.IEX_TOKEN, symbol) # lookup api  method

screen = st.sidebar.selectbox("View", ('Overview', 'Fundamentals', 'News', 'Ownership', 'Technicals'), index=0)

st.title(screen)

c = p.Client(api_token=config.api_key, version='stable')

logo = c.logo(symbol=symbol)

def df_to_sql(df, table_name=f'{symbol}'):
    """
    THIS METHOD WRITES THE DATAFRAME PASSED TO A TABLE
    """

    conn_string = f'postgresql://{config.DB_USER}:{config.DB_PASSWORD}@{config.DB_HOST}/{config.DB_NAME}'
    engine = create_engine(conn_string)
    df.to_sql(table_name, engine)


if screen == 'Overview':

    st.image(logo['url'])

    quote = c.quoteDF(symbol=symbol)

    st.write(f'{symbol} Quote')
    write_quote = st.button('Write quote to db')

    if write_quote:
        df_to_sql(quote, table_name=f'{symbol}_quote')

    st.dataframe(quote)

    timeframe = st.selectbox('Select', ["5dm", "5d", "1mm", "1m", "3m", "6m", "ytd", "1yr", "2y", "5y", "max", "dynamic"], index=4)
    chart = c.chartDF(symbol=symbol, timeframe=timeframe)[['open', 'high', 'low','close', 'volume']]

    st.write(f'{symbol} Chart')
    write_chart = st.button('Write chart to db')

    if write_chart:
        df_to_sql(chart, table_name=f'{symbol}_chart')

    st.dataframe(chart)


if screen == 'News':

    st.image(logo['url'])

    st.write(f"{symbol} Story Count")
    count = st.selectbox('Select', ["10", "20", "50", "100"], index=1)
    news = c.newsDF(symbol=symbol, count=count)[['headline', 'source']]
    st.dataframe(news)

if screen == 'Fundamentals':
    pass

if screen == 'Ownership':
    pass
   