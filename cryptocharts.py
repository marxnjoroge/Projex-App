import streamlit as st
import pandas as pd
import requests as rq
import yfinance as yf
import plotly.graph_objects as go
import plotly.express as px
import plotly.animation as panya
import numpy as np
import json as json
import streamlit.components.v1 as components
import random
import matplotlib.pyplot as plt
import matplotlib.animation as anim
from datetime import datetime as dt,timedelta
import pybase64

st.write("Coinbase Pro Currency Chart (1 min. OHLC basis)")

def st_display_pdf(pdf_file):
    with open(pdf_file, "rb") as f:
        base64_pdf = pybase64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<embed src="data:application/pdf;pybase64,{base64_pdf}” width=”700″ height=”1000″ type=”application/pdf”>'
    st.markdown(pdf_display, unsafe_allow_html=True)
expand = st.expander("About")
expand.markdown("""
* **Python Libraries:** streamlit, streamlit.components, pandas, requests, 
matplotlib, matplotlib.animation, time, random, json, plotly.
* ** Data sources:** [Coinpaprika] (https://coinpaprika.com), [Getblock.io] (https://getblock.io), [Coinbase Pro] (https://pro.cloud.coinbase.com), [Yahoo Finance] (https://yahoo.com/finance).
* ** APIs:** rpc/application, [Rosetta] (https://www.rosetta-api.org/docs/BlockApi.html) API, [XRP Ledger API] (https://xrpl.org/).
* ** Layout:** Thanks to [Data Professor] (https://www.youtube.com/channel/UCV8e2g4IWQqK71bbzGDEI4Q0) for 
    streamlit tips and tricks.
* ** Authored by:** Marx Njoroge, ©2024. 
* ** Immesurable thanks to [Neal Stephenson] (https://www.nealstephenson.com/). 
    """) 
with st.sidebar:
    sym = st.text_input("Enter Currency Pair Symbol (Coinbase Listings):", "ETH_USD", max_chars=None).upper()

st.title("Crypto Coin Data")

cb_api_url = "https://go.coinbase.com"
bar_size = 3600
timeend = dt.now()
delta = timedelta(hours=1)
timestart = timeend - (168 * delta)

timeend = timeend.isoformat()
timestart = timestart.isoformat()

params = {
    "start": timestart,
    "end": timeend,
    "granularity": bar_size,
}
cb_headers = {"Content-Type": "application/json"}

cb_data = rq.get(f"{cb_api_url}/products/{sym}/candles",
                    json = params,
                    headers = cb_headers
)

print(cb_data)

# st.subheader(f"{sym}: ${cb_data[0][4]} | {dt.fromtimestamp(cb_data[0][0]).strftime('%Y.%m.%d %H:%M:%S')}")

# minselect = st.sidebar.select_slider("Time Delta", ["ONE_MINUTE", "FIVE_MINUTE", "FIFTEEN_MINUTET", "THIRTY_MINUTE", "ONE_HOUR", "TWO_HOUR", "SIX_HOUR", "ONE_DAY"])

# df = pd.DataFrame(cb_data,
#                     columns=['time', 'low', 'high', 'open', 'close', 'volume']
#                     )
# df['date'] = pd.to_datetime(df['time'], unit='s')
# df = df[['date', 'low', 'high', 'open', 'close', 'volume']]
# df.set_index('date', inplace=True)
# df = df.resample(minselect).agg(
#     {
#     "date": "date",
#     "open": "first",
#     "high": "max",
#     "low": "min",
#     "close": "last",
#     "volume": "max"
#     }
# )
# df.reset_index("date", inplace=True)

# fig = go.Figure(data=[go.Candlestick(
#     x=df["date"],
#     open=df["open"],
#     high=df['high'],
#     low=df['low'],
#     close=df['close'],
#     name=sym,
#     increasing_line_color='magenta',
#     decreasing_line_color='lightgrey'
#             )
#         ]
#     )
# fig.update_xaxes(type='category')
# fig.update_layout(height=600, width=800)

# st.plotly_chart(fig, use_container_width=True)

# st.write("Coinbase Pro Currency Data")

# st.dataframe(df)
# st.write(df)

# tickerData = yf.Ticker(symbol)
# tickerDf = tickerData.history(period='ytd', interval='1d')
#
# st.line_chart(tickerDf.Close)
# st.image(f"https://finviz.com/chart.ashx?t={symbol}")
