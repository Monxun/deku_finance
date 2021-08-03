import streamlit as st
import deku_methods as dm
import pyEX as p
import config
import pandas

print("Initializing gui...")

symbol = st.sidebar.text_input("Symbol", value='GME')

screen = st.sidebar.selectbox("View", ('Overview', 'Fundamentals', 'News', 'Ownership', 'Technicals'), index=0)

st.title(screen)

c = p.Client(api_token=config.api_key, version='stable')


if screen == 'Overview':

    quote = c.quoteDF(symbol=symbol)

    st.write(f'{symbol} Quote')
    st.dataframe(quote)

    timeframe = st.selectbox('Select', ["5dm", "5d", "1mm", "1m", "3m", "6m", "ytd", "1yr", "2y", "5y", "max", "dynamic"], index=4)
    chart = c.chartDF(symbol=symbol, timeframe=timeframe)[['open', 'high', 'low','close', 'volume']]

    st.write(f'{symbol} Chart')
    st.dataframe(chart)

if screen == 'News':

    st.write(f'{symbol} Quote')
    st.write("Story Count")
    count = st.selectbox('Select', ["10", "20", "50", "100"], index=1)
    news = c.newsDF(symbol=symbol, count=count)[['headline', 'source']]
    st.dataframe(news)

if screen == 'Fundamentals':
    pass

if screen == 'Ownership':
    pass
  