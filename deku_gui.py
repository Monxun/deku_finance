import streamlit as st
import deku_methods as dm
import pyEX as p
import config
import pandas

print("Initializing gui...")
st.title('DEKU_FINANCE')
c = p.Client(api_token=config.api_key, version='stable')

sym='TWTR'
d = c.quoteDF(symbol=sym)

st.write('Hello')
st.dataframe(d)