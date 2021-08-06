
import os
import time
import pandas as pd
from sqlalchemy import create_engine
import psycopg2
import config
import streamlit as st
import yfinance as yf

#'SYMBOL' ST TEXT INPUT OBJECT
symbol = st.sidebar.text_input("Symbol", value='GME')

#INPUT YOUR OWN CONNECTION STRING HERE
def df_to_sql(df, table_name=f'{symbol}'):
    """
    THIS METHOD WRITES THE DATAFRAME PASSED TO A TABLE
    """

    conn_string = f'postgresql://{config.DB_USER}:{config.DB_PASSWORD}@{config.DB_HOST}/{config.DB_NAME}'
    engine = create_engine(conn_string)
    df.to_sql(table_name, engine)

#INITIALIZE DATA API OBJECT
symbol_get = yf.Ticker(symbol)

#GET HISTORICAL DATA
hist = symbol_get.history(period="5d")

#DISPLAY HEAD IN GUI
st.dataframe(hist.head())

#WRITE TO CSV
hist.to_csv(f'{symbol}.csv', index = True)

#CALL df_to_sql() METHOD
df_to_sql(hist)