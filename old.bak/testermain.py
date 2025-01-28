import streamlit as st
import pandas as pd
import requests as rq
import yfinance as yf
import plotly.graph_objects as go
import plotly.express as px
import plotly.animation as panya
import numpy as np
import json
import streamlit.components.v1 as components
import random
import matplotlib.pyplot as plt
import matplotlib.animation as anim
from datetime import datetime as dt,timedelta
from groq import Groq

# def add_logo_to_sidebar():
#     # CSS styles for the logo animation
#     st.markdown(
#         """
#         <style>
#             [data-testid="stSidebarNav"] {
#                 background-image: none;
#                 padding-top: 100px;
#             }
#             [data-testid="stSidebarNav"]::before {
#                 content: "";
#                 display: block;
#                 width: 100%;
#                 height: 20px;
#                 position: absolute;
#                 top: 0;
#                 left: 0;
#                 background-color: white;
#                 overflow: hidden;
#             }
            
#             [data-testid="stSidebarNav"]::after {
#                 content: "";
#                 margin-left: 10px;
#                 width: calc(100% - 10px);
#                 height: 80px;
#                 position: absolute;
#                 top: 10px;
#                 left: 0;
#                 background: #1A365D;
#                 overflow: hidden;
#             }
            
#             .logo-text {
#                 position: absolute;
#                 top: 35px;
#                 left: 60px;
#                 font-family: Arial, sans-serif;
#                 font-weight: bold;
#                 font-size: 42px;
#                 z-index: 1000;
#             }
            
#             .text-pro {
#                 color: #E2E8F0;
#                 animation: pulse 4s infinite;
#             }
            
#             .text-jex {
#                 color: #90CDF4;
#                 animation: pulse 4s infinite;
#                 animation-delay: 2s;
#             }
            
#             .circuit-line {
#                 position: absolute;
#                 background: #4299E1;
#                 opacity: 0.2;
#                 z-index: 999;
#             }
            
#             .horizontal {
#                 height: 1px;
#                 width: calc(100% - 40px);
#                 margin-left: 20px;
#             }
            
#             .vertical {
#                 width: 1px;
#                 height: 80px;
#                 top: 10px;
#             }
            
#             .h1 { top: 20px; animation: glowH 4s infinite; }
#             .h2 { top: 50px; animation: glowH 4s infinite 1s; }
#             .h3 { top: 80px; animation: glowH 4s infinite 2s; }
            
#             .v1 { left: 60px; animation: glowV 4s infinite 0.5s; }
#             .v2 { left: 160px; animation: glowV 4s infinite 1.5s; }
#             .v3 { left: 260px; animation: glowV 4s infinite 2.5s; }
            
#             .circle {
#                 width: 16px;
#                 height: 16px;
#                 position: absolute;
#                 top: 35px;
#                 border-radius: 50%;
#                 z-index: 1000;
#             }
            
#             .circle1 {
#                 right: 90px;
#                 background: #90CDF4;
#                 animation: pulse 4s infinite;
#             }
            
#             .circle2 {
#                 right: 60px;
#                 background: #E2E8F0;
#                 animation: pulse 4s infinite 2s;
#             }
            
#             @keyframes glowH {
#                 0%, 100% { opacity: 0.1; }
#                 50% { opacity: 0.3; }
#             }
            
#             @keyframes glowV {
#                 0%, 100% { opacity: 0.1; }
#                 50% { opacity: 0.3; }
#             }
            
#             @keyframes pulse {
#                 0%, 100% { opacity: 0.8; }
#                 50% { opacity: 1; }
#             }
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

#     # HTML for the logo
#     st.markdown(
#         """
#         <div class="logo-text">
#             <span class="text-pro">PRO</span><span class="text-jex">JEX</span>
#         </div>
#         <div class="circuit-line horizontal h1"></div>
#         <div class="circuit-line horizontal h2"></div>
#         <div class="circuit-line horizontal h3"></div>
#         <div class="circuit-line vertical v1"></div>
#         <div class="circuit-line vertical v2"></div>
#         <div class="circuit-line vertical v3"></div>
#         <div class="circle circle1"></div>
#         <div class="circle circle2"></div>
#         """,
#         unsafe_allow_html=True
#     )

# # Example usage in your Streamlit app
# def main():
#     st.set_page_config(layout="wide", page_title="Projex")
        
#     # Your other Streamlit app content here
#     st.title("Projex")

# if __name__ == "__main__":
#     main()

st.set_page_config(layout="wide", page_title="Projex")
padding = 3
st.markdown(""" <style>    
    .reportview-container .main .block-container{{
        padding-top: {padding}rem;
        padding-right: {padding}rem;
        padding-left: {padding}rem;
        padding-bottom: {padding}rem;
    }} </style> """, unsafe_allow_html=True)

hide_menu_style = """ <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden; }
        </style> """

st.markdown(hide_menu_style, unsafe_allow_html=True)

# @st.cache_data
def load_data():
    url = "https://finviz.com/crypto_performance.ashx"
    html = pd.read_html(url, header=0)
    dfcrypto = html[0]
    st.dataframe(dfcrypto)
    return dfcrypto

# load_crypto_data()

# Sorting Algorithms.

def bubbleSort(arr):

    yield arr
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            yield (*arr,)


def mergeSort(arr):

    if len(arr) > 1:
        mid = len(arr) // 2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]

        yield from mergeSort(lefthalf)
        yield from mergeSort(righthalf)

        # These are indexes: i for lefthalf, j for righthalf, k for nlist.
        i = j = k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                arr[k] = lefthalf[i]
                i = i+1
            else:
                arr[k] = righthalf[j]
                j = j+1
            k = k+1
            yield (*arr,)
        while i < len(lefthalf):
            arr[k] = lefthalf[i]
            i = i+1
            k = k+1
            yield (*arr,)
        while j < len(righthalf):
            arr[k] = righthalf[j]
            j = j+1
            k = k+1
            yield (*arr,)
        yield (*arr,)
    yield (*arr,)


def quickSort(arr, left, right):
    yield arr
    if left < right and len(arr) > 1:
        pivotindex = int(partition(arr, left, right))
        yield from quickSort(arr, left, pivotindex - 1)
        yield from quickSort(arr, pivotindex + 1, right)
    yield (*arr,)


def partition(arr, left, right):
    i = left
    j = right - 1
    pivot = arr[right]

    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]

    return i


sidebar = st.sidebar
col2, col3 = st.columns((2,1))

# ------------------------------- #

# Sidebar + Main panel

# with sidebar:
#     add_logo_to_sidebar()

sidebar.header("Python Projects \n(Press 'r' or 'R' to refresh)")

# option = sidebar.selectbox("Tools", ('Cryptonomics', 'Cryptocurrency Top 100', 'Crypto Charts', 'Large Language Models', 'Blockchain Explorer', 'Sort Visualizations'))
option = sidebar.selectbox("Tools", ('Projex', 'AI Assistant', 'Blockchain Explorer', 'Sort Visualizations'))

if option == 'Projex':

    st.header("Python Projects")

    st.write("Welcome to Projex, a platform showcasing innovative projects that push the boundaries of technology and innovation. As hiring managers, you're likely looking for talented individuals who can bring cutting-edge skills and expertise to your team. This project website is designed to give you a glimpse into the exciting work being done by our developers, and to help you identify top talent who can drive your organization forward.")
    
    st.write("On this website, you'll find three distinct projects that demonstrate our team's capabilities in various areas of technology:")

    "Blockchain Explorer: The Blockchain Explorer is a comprehensive platform for exploring and analyzing blockchain transactions, providing insights into network activity, transaction patterns, and more. This project showcases our team's expertise in blockchain development, data analysis, and visualization."  

    "Large Language Model: This Large Language Model wrapper is an AI application that leverages the power of machine learning to analyze and generate human-like text. This project highlights our team's skills in natural language processing, machine learning, and software development."  

    "Sort Visualizer: This Sort Visualizer is an interactive web application that illustrates the process of sorting algorithms, providing a visual representation of complex data structures and algorithmic processes. This project demonstrates our team's ability to design and develop engaging user interfaces, as well as their understanding of computer science concepts."  

    "By exploring these projects, you'll gain a deeper understanding of our team's capabilities and expertise in areas such as blockchain development, AI, machine learning, and software engineering. Whether you're looking to fill a specific role or seeking to bring in a team of talented developers, we believe that our projects will give you a compelling reason to consider our team for your organization's needs."  

    "I am excited for feature updates to these projects and look forward to the opportunity to collaborate on upcoming projects."

if option == 'AI Assistant':

    llms = ['Meta LlaMa3', 'Google gemma2-9b-it', 'Mistral mixtral-8x7b-32768']
    default_llm = 'Meta LlaMa3'
    model = ""
    ident2 = "lmodel"
    title = st.sidebar.pills("Popular Models:", llms, default=("Meta LlaMa3"))
    if title == 'Meta LlaMa3':
        model = "llama3-8b-8192"

    if title == 'Google gemma2-9b-it':
        model = "gemma2-9b-it"

    if title == 'Mistral mixtral-8x7b-32768':
        model = 'mixtral-8x7b-32768'
    
    st.title("AI Assistant Chat")

    st.markdown(''':gray[_Powered by_:/~>]''' +title)
    st.markdown("This chat is tuned toward the technical.  Enter a query below and learn something new.")
    st.divider()

    client = Groq(api_key=st.secrets.get("GROQ_API_KEY"))

    if "default_model" not in st.session_state:
        st.session_state["default_model"] = "llama3-8b-8192"

    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    print(st.session_state.messages)

# Clear messages from responses.
    with st.sidebar:

        st.divider()

        def handle_click():
            st.session_state.messages = []

        reset = st.button(label="Reset Chat", on_click=handle_click)
        
# Show Messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

# Input prompt for user queries.
    if prompt := st.chat_input():
        st.session_state.messages.append({"role": "user", "content": prompt})


        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            response_text = st.empty()

            completion = client.chat.completions.create(
                temperature = 0.5,
                n = 1,
                model = model,
                max_tokens = 1024,
                messages = [
                {"role": m["role"], "content": m["content"]} 
                for m in st.session_state.messages
                ],
                stream = True,
            )

            response = ""

            for chunk in completion:
                response += chunk.choices[0].delta.content or ""
                response_text.markdown(response)

            st.session_state.messages.append({"role": "assistant", "content": response})
    

if option == 'Sort Visualizations':
    col2.header(option)
    title = st.sidebar.radio(label="Sort Algorithms", options=["Merge", "Quick", "Bubble"])

    if title == 'Merge':

        col2.subheader(title)

        st.write("This visualization is written in Python using Matplotlib "
                 "to both visualize and animate the Sort Algorithm.  A Streamlit "
                 "component is then used to dynamically convert the Matplotlib animation "
                 "to javascript in order to render it to html.")
        st.write("**Note:** sorting more values takes longer to render.")

        
        with sidebar:
            n = st.slider(label="No. of Array Values", min_value=15, max_value=50)
        alg = 2
        cache = n * 10
        title = "Merge Sort"
        array = [i + 1 for i in range(n)]
        random.shuffle(array)
        algo = mergeSort(array)

        # Initialize fig
        plt.rcParams["figure.figsize"] = (7, 4)
        plt.rcParams["font.size"] = 8
        # with _lock:
        fig, ax = plt.subplots()
        ax.set_title(title)

        bar_rec = ax.bar(range(len(array)), array, align='edge')

        ax.set_xlim(0, n)
        ax.set_ylim(0, int(n * 1.06))

        text = ax.text(0.02, 0.95, "0", transform=ax.transAxes)

        epochs = [0]


        def init():
            ax.bar(range(len(array)), array, align='edge')

        # @st.cache
        def update_plot(array, rect, epochs):
            for rect, val in zip(rect, array):
                rect.set_height(val)
                rect.set_color("#cc00cc")
            text.set_text("No. of operations: {}".format(epochs[0]))
            epochs[0] += 1

            return bar_rec,


        anima = anim.FuncAnimation(fig, update_plot, fargs=(bar_rec, epochs), frames=algo, save_count=cache, interval=20,
                                       repeat=False)
        # plt.show()
        # st.pyplot(plt)

        components.html(anima.to_jshtml(), height=1000)

    if title == 'Quick':
        st.subheader(title)

        st.write("This visualization is written in Python using Matplotlib "
                 "to both visualize and animate the Sort Algorithm.  A Streamlit "
                 "component is then used to dynamically convert the Matplotlib animation "
                 "to javascript in order to render it to html.")
        st.write("**Note:** sorting more values takes longer to render.")
        with sidebar:
            n = st.slider(label="No. of Array Values", min_value=15, max_value=50)
        alg = 3
        cache = 500
        title = "Quick Sort"
        array = [i + 1 for i in range(n)]
        random.shuffle(array)
        algo = quickSort(array, 0, len(array) - 1)

        # Initialize fig
        # with _lock:
        plt.rcParams["figure.figsize"] = (7, 4)
        plt.rcParams["font.size"] = 8
        fig, ax = plt.subplots()
        ax.set_title(title)

        bar_rec = ax.bar(range(len(array)), array, align='edge')

        ax.set_xlim(0, n)
        ax.set_ylim(0, int(n * 1.06))

        text = ax.text(0.02, 0.95, "0", transform=ax.transAxes)

        epochs = [0]


        def init():
            ax.bar(range(len(array)), array, align='edge', color="#0033ff")

        # @st.cache
        def update_plot(array, rect, epochs):
            for rect, val in zip(rect, array):
                rect.set_height(val)
                rect.set_color("#33cccc")
            text.set_text("No. of operations: {}".format(epochs[0]))
            epochs[0] += 1

            return bar_rec,


        anima = anim.FuncAnimation(fig, update_plot, fargs=(bar_rec, epochs), frames=algo, save_count=cache, interval=20,
                                   repeat=False)
        # plt.show()
        # st.pyplot(plt)

        components.html(anima.to_jshtml(), height=1000)

    if title == 'Bubble':
        st.subheader(title)

        st.write("This visualization is written in Python using Matplotlib "
                 "to both visualize and animate the Sort Algorithm.  A Streamlit "
                 "component is then used to dynamically convert the Matplotlib animation "
                 "to javascript in order to render it to html.")
        st.write("** Note:** sorting more values takes longer to render.")

        with sidebar:
            n = st.slider(label="No. of Array Values", min_value=15, max_value=50)
        alg = 1
        cache = n * (n**1/2)
        title = "Bubble Sort"
        array = [i + 1 for i in range(n)]
        random.shuffle(array)
        algo = bubbleSort(array)

        # Initialize fig with mathplotlib:
        data = np.random.randint(1, 100, size=n)

        # Create figure and axes
        fig, ax = plt.subplots()
        bars = ax.bar(range(len(data)), data, color='blue')

        # Function to update bar positions for each frame
        def animate(i):
            global data
            for j in range(len(data) - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
                    bars[j].set_height(data[j])
                    bars[j + 1].set_height(data[j + 1])
            return bars

        # Create the animation
        ani = anim.FuncAnimation(fig, animate, frames=len(data)-1, interval=50, blit=True)

        # Display the animation using Streamlit
        components.html(ani.to_jshtml(), height=800)

        # An test to replace mathplotlib with plotyly:

        n = 25
        alg = 1
        cache = n * (n**0.5)
        title = "Bubble Sort"
        array = [i + 1 for i in range(n)]
        random.shuffle(array)
        algo = bubbleSort(array)

        fig = go.Figure(data=[go.Bar(x=range(len(array)), y=array, marker_color="#cccccc")])

        fig.update_layout(title=title, xaxis_title="", yaxis_title="")
        fig.update_xaxes(range=[0, n])
        fig.update_yaxes(range=[0, int(n * 1.06)])

        text = go.Annotation(text="0", x=0.02, y=0.95, xref="paper", yref="paper", showarrow=False)

        epochs = [0]

        def init():
            fig.data[0].marker.color = "#00cccc"

        def update(array):
            for i, val in enumerate(array):
                fig.data[0].y[i] = val
                fig.data[0].marker.color[i] = "#cc00cc"
            text.text = f"No. of operations: {epochs[0]}"
            epochs[0] += 1
            return fig,

        fig.update_layout(annotations=[text])
        fig.update_layout(xaxis=dict(rangeslider=dict(visible=True), type="date"))

        fig.show()

if option == 'Blockchain Explorer':

    col2.header("Placeholder")
    title = st.sidebar.radio(label="Latest Blocks from:", options=["Bitcoin: BTC", "Ethereum: ETH", "Binance Smart Chain: BNB", "Ripple: XRP"])

    # title = st.sidebar.radio(label="Latest Blocks from:", options=["Bitcoin: BTC", "Ethereum: ETH", "Binance Smart Chain: BNB", "Cardano: ADA", "Ripple: XRP"])

    if title == "Bitcoin: BTC":

        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSJEz7ChxRTdUyUh3dXCBb6WaTThx3O6VzKdQ&usqp=CAU")
        st.subheader("Bitcoin RPC API")
        st.write("""Using Getblock's Blockchain Node Provider for access to BTC network and data.""")
        st.write("""**Note:** Data returned from API calls are chain-specific.""")

        GETBLOCK_BTC_TOKEN = st.secrets["GETBLOCK_BTC_TOKEN"]
        btc_status_endpoint = "https://go.getblock.io/"+GETBLOCK_BTC_TOKEN
        headers = {
            "X-API-TOKEN": st.secrets["GETBLOCK_BTC_TOKEN"],
        }

        @st.cache_data
        def get_latest_block():

            btc_status_params = {
                
                "jsonrpc": "2.0",
                "id": "bitcoin",
                "method": "getblockchaininfo",
                "id": "getblock.io"
            }

            btc_chaindata = rq.post(url=btc_status_endpoint, json=btc_status_params, headers=headers).json()
            blockhash = btc_chaindata['result']['bestblockhash']

            return blockhash


        latest_blockhash = get_latest_block()

        btc_hash = latest_blockhash
        lastn = []

        index = []
        time = []
        blockhash = []
        blocksize = []
        nTx = []
        btc_txs = []

        for i in range(0, 10):
            last_block_params = {
                "jsonrpc": "2.0",
                "id": "bitcoin",
                "method": "getblock",
                "params": [btc_hash]
            }
            new_block = {}
            btc_blockdata = rq.post(url=btc_status_endpoint, json=last_block_params, headers=headers).json()
            new_block['index'] = btc_blockdata['result']['height']
            new_block['timestamp'] = btc_blockdata['result']['time']
            new_block['blockhash'] = btc_blockdata['result']['hash']
            new_block['blocksize'] = btc_blockdata['result']['size']
            new_block['nTx'] = btc_blockdata['result']['nTx']
            index.append(new_block['index'])
            time.append(dt.fromtimestamp(new_block['timestamp']).strftime('%Y.%m.%d %H:%M:%S'))
            blockhash.append(new_block['blockhash'])
            blocksize.append(new_block['blocksize'])
            nTx.append(new_block['nTx'])
            btc_txs.append(btc_blockdata['result']['tx'][:20])

            lastn.append(new_block)
            btc_hash = btc_blockdata['result']['previousblockhash']

        st.write("\nLatest Blocks\n")
        df = pd.DataFrame(columns=['index', 'timestamp (utc)', 'blockhash', 'blocksize', 'no.transactions'])

        df['index'] = index
        df['timestamp (utc)'] = time
        df['blockhash'] = blockhash
        df['blocksize'] = blocksize
        df['no.transactions'] = nTx

        # df = df.style.hide_index()
        st.dataframe(df)

        blocktime = []
        confirmations = []
        size = []
        txid = []
        value = []
        hash = []

        for i in range(0, 20):
            btc_txs_params = {
                "jsonrpc": "2.0",
                "method": "getrawtransaction",
                "params": {
                    "txid": btc_txs[0][i],
                    "verbose": True
                },
                "id": "getblock.io"
            }

            btc_txs_data = rq.post(url=btc_status_endpoint, json=btc_txs_params, headers=headers).json()
            # btc_txs_summary.append(btc_txs_data['result'])
            blocktime.append(dt.fromtimestamp(btc_txs_data['result']['blocktime']).strftime('%Y.%m.%d %H:%M:%S'))
            confirmations.append(btc_txs_data['result']['confirmations'])
            size.append(btc_txs_data['result']['size'])
            txid.append(btc_txs_data['result']['txid'])
            value.append(btc_txs_data['result']['vout'][0]['value'])
            hash.append(btc_txs_data['result']['hash'])

        st.write("\nLatest Transactions\n")
        dftx = pd.DataFrame(columns=['blocktime', 'confirmations', 'size', 'txid', 'value (BTC)', 'hash'])

        dftx['blocktime'] = blocktime
        dftx['confirmations'] = confirmations
        dftx['size'] = size
        dftx['txid'] = txid
        dftx['value (BTC)'] = value
        dftx['hash'] = hash

        # dftx = dftx.style.hide_index()

        st.dataframe(dftx)

    if title == "Ethereum: ETH":

        # @st.cache_resource
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRvWkHiF5KiIrH-bQmqr19sodbZCBz3uLRrxQ&usqp=CAU")
        st.subheader("Ethereum RPC API")
        st.write("""Using Getblock's Blockchain Node Provider for access to Ethereum network and data.""")
        st.write("""**Note:** Data returned from API calls are chain-specific.""")

        GETBLOCK_ETH_TOKEN = st.secrets["GETBLOCK_ETH_TOKEN"]
        GETBLOCK_ETH_URL = "https://go.getblock.io/"+GETBLOCK_ETH_TOKEN
        
        eth_headers = {
            "X-API-KEY": GETBLOCK_ETH_TOKEN
        }

        blocknumber = []
        timestamp = []
        blockhash = []
        gasLimit = []
        gasUsed = []

        latest_blocks = []
        block_num = "latest"
        eth_params = {
            "id": "blockNumber",
            "jsonrpc": "2.0",
            "method": "eth_getBlockByNumber",
            "params": [block_num, False]
        }
        eth_blockdata = rq.post(url=GETBLOCK_ETH_URL, json=eth_params, headers=eth_headers).json()
        curr_block_hash = eth_blockdata['result']['hash']
        curr_block_number = eth_blockdata['result']['number']
        curr_txs_hash = []

        for i in range(0, 10):
            hash_eth_params = {
                "id": "blockHash",
                "jsonrpc": "2.0",
                "method": "eth_getBlockByHash",
                "params": [curr_block_hash, False]
            }
            hash_eth_blockdata = rq.post(url=GETBLOCK_ETH_URL, json=hash_eth_params, headers=eth_headers).json()
            new_block = {'blocknumber': hash_eth_blockdata['result']['number'],
                            'timestamp': hash_eth_blockdata['result']['timestamp'],
                            'blockhash': hash_eth_blockdata['result']['hash'],
                            'gasLimit': hash_eth_blockdata['result']['gasLimit'],
                            'gasUsed': hash_eth_blockdata['result']['gasUsed']}

            latest_blocks.append(new_block)
            if i == 0:
                curr_txs_hash.append(hash_eth_blockdata['result']['transactions'][:20])
            curr_block_hash = hash_eth_blockdata['result']['parentHash']

        dec_blocks = []
        for dc in latest_blocks:
            dc['blocknumber'] = int(dc['blocknumber'], 16)
            dc['timestamp'] = int(dc['timestamp'], 16)
            dc['gasLimit'] = int(dc['gasLimit'], 16)
            dc['gasUsed'] = int(dc['gasUsed'], 16)
            blocknumber.append(dc['blocknumber'])
            timestamp.append(dt.fromtimestamp(dc['timestamp']).strftime('%Y.%m.%d %H:%M:%S'))
            blockhash.append(dc['blockhash'])
            gasLimit.append(dc['gasLimit'])
            gasUsed.append(dc['gasUsed'])

            dec_blocks.append(dc)

        df = pd.DataFrame(columns=['blocknumber', 'timestamp (utc)', 'blockhash', 'gasLimit', 'gasUsed'])
        df['blocknumber'] = blocknumber
        df['timestamp (utc)'] = timestamp
        df['blockhash'] = blockhash
        df['gasLimit'] = gasLimit
        df['gasUsed'] = gasUsed

        st.write("\nLatest Blocks\n")
        st.dataframe(df)

        transx_blockid = []
        trans_idx = []
        gas = []
        gas_price = []
        from_acct = []
        to_acct = []
        value = []
        type = []

        for i in range(0, 20):
            hash_eth_params = {
                "id": "txsHash",
                "jsonrpc": "2.0",
                "method": "eth_getTransactionByHash",
                "params": [curr_txs_hash[0][i]]
            }
            hash_eth_txdata = rq.post(url=GETBLOCK_ETH_URL, json=hash_eth_params, headers=eth_headers).json()
            transx_blockid.append(int(hash_eth_txdata['result']['blockNumber'], 16))
            trans_idx.append(int(hash_eth_txdata['result']['transactionIndex'], 16))
            gas.append(int(hash_eth_txdata['result']['gas'], 16))
            gas_price.append(int(hash_eth_txdata['result']['gasPrice'], 16))
            from_acct.append(hash_eth_txdata['result']['from'])
            to_acct.append(hash_eth_txdata['result']['to'])
            value.append(int(hash_eth_txdata['result']['value'], 16))
            type.append(int(hash_eth_txdata['result']['type'], 16))

        txdf = pd.DataFrame(
            columns=['transx_blockid', 'trans_idx', 'gas', 'gas_price', 'from_acct', 'to_acct', 'value (WEI)', 'type'])
        txdf['transx_blockid'] = transx_blockid
        txdf['trans_idx'] = trans_idx
        txdf['gas'] = gas
        txdf['gas_price'] = gas_price
        txdf['from_acct'] = from_acct
        txdf['to_acct'] = to_acct
        txdf['value'] = value
        txdf['type'] = type

        # st.write("\nLatest Transactions\n")
        # st.dataframe(txdf)

    # if title == "Cardano: ADA":

    #     col2.image("cardanosizedlogo.svg")
    #     st.subheader("Cardano [Rosetta] (https://www.rosetta-api.org/docs/BlockApi.html) API.")
    #     st.write("""Using Getblock's Blockchain Node Provider for access to the Cardano network and data.""")
    #     st.write("""**Note:** Data returned from API calls are chain-specific.""")

    #     ada_status_endpoint = "https://goada.getblock.io/"
    #     GETBLOCK_API_TOKEN = st.secrets["GETBLOCK_API_TOKEN"]
    #     headers = {
    #         "X-API-KEY": GETBLOCK_API_TOKEN,
    #         "Content-Type": "application/json"
    #     }

    #     status_params = {
    #         "network_identifier": {
    #             "blockchain": "cardano",
    #             "network": "mainnet"},
    #         "metadata": {}
    #     }

    #     ada_status = rq.post(url=ada_status_endpoint, json=status_params, headers=headers).json()
    #     # pprint(ada_status)
    #     curr_block_idx = ada_status['current_block_identifier']['index']
    #     curr_block_hash = ada_status['current_block_identifier']['hash']
    #     latest_blocks = []

    #     epoch = []
    #     index = []
    #     timestamp = []
    #     blockhash = []
    #     blocksize = []

    #     for i in range(0, 20):
    #         ada_block_endpoint = "https://go.getblock.io/"
    #         block_params = {
    #             "network_identifier": {
    #                 "blockchain": "cardano",
    #                 "network": "mainnet"},
    #             "metadata": {},
    #             "block_identifier": {
    #                 "index": curr_block_idx,
    #                 "hash": curr_block_hash}
    #         }

    #         block_data = rq.post(url=ada_block_endpoint, json=block_params, headers=headers).json()
    #         new_block = {'epoch': block_data['block']['metadata']['epochNo'],
    #                         'index': block_data['block']['block_identifier']['index'],
    #                         'timestamp': block_data['block']['timestamp'],
    #                         'blockhash': block_data['block']['block_identifier']['hash'],
    #                         'blocksize': block_data['block']['metadata']['size']}
    #         epoch.append(new_block['epoch'])
    #         index.append(new_block['index'])
    #         timestamp.append(dt.fromtimestamp((new_block['timestamp'])/1000).strftime('%Y.%m.%d %H:%M:%S'))
    #         blockhash.append(new_block['blockhash'])
    #         blocksize.append(new_block['blocksize'])

    #         latest_blocks.append(new_block)

    #         curr_block_idx = block_data['block']['parent_block_identifier']['index']
    #         curr_block_hash = block_data['block']['parent_block_identifier']['hash']

    #     df = pd.DataFrame(columns=['epoch', 'index', 'timestamp (utc)', 'blockhash', 'blocksize'])
    #     df['epoch'] = epoch
    #     df['index'] = index
    #     df['timestamp (utc)'] = timestamp
    #     df['blockhash'] = blockhash
    #     df['blocksize'] = blocksize

    #     st.dataframe(df)
    #     #st.json(latest_blocks)

    if title == "Binance Smart Chain: BNB":

        st.image("images/330px-Binance_logo.svg.png")
        st.subheader(f"Binance Smart Chain (BNB): Ethereum RPC API")
        st.write("""Using Getblock's Blockchain Node Provider for access to Binance Smart Chain network and data.""")
        st.write("""**Note:** Data returned from API calls are chain-specific.""")

        GETBLOCK_BSC_TOKEN = st.secrets["GETBLOCK_BSC_TOKEN"]
        GETBLOCK_BSC_URL = "https://go.getblock.io/"+GETBLOCK_BSC_TOKEN

        bsc_headers = {
            "X-API-KEY": GETBLOCK_BSC_TOKEN,
            "Content-Type": "application/json"
        }

        blocknumber = []
        timestamp = []
        size = []
        blockhash = []
        gasLimit = []
        gasUsed = []
        miner = []

        latest_blocks = []
        curr_block_num = "latest"

        num_bsc_params = {
            "id": "binance",
            "jsonrpc": "2.0",
            "method": "eth_getBlockByNumber",
            "params": [curr_block_num, True]
        }
        num_bsc_blockdata = rq.post(url=GETBLOCK_BSC_URL, json=num_bsc_params, headers=bsc_headers).json()

        curr_block_hash = num_bsc_blockdata['result']['hash']
        curr_txs_hash = []
        # print(curr_block_hash)

        for i in range(0, 10):
            hash_bsc_params = {
                "id": "binance",
                "jsonrpc": "2.0",
                "method": "eth_getBlockByHash",
                "params": [curr_block_hash, True]
            }

            hash_bsc_blockdata = rq.post(url=GETBLOCK_BSC_URL, json=hash_bsc_params, headers=bsc_headers).json()
            # print(hash_bsc_blockdata)
            new_block = {'blocknumber': hash_bsc_blockdata['result']['number'],
                            'timestamp': hash_bsc_blockdata['result']['timestamp'],
                            'size': hash_bsc_blockdata['result']['size'],
                            'blockhash': hash_bsc_blockdata['result']['hash'],
                            'gasLimit': hash_bsc_blockdata['result']['gasLimit'],
                            'gasUsed': hash_bsc_blockdata['result']['gasUsed'],
                            'miner': hash_bsc_blockdata['result']['miner']}

            latest_blocks.append(new_block)
            if i == 0:
                curr_txs_hash.append(hash_bsc_blockdata['result']['transactions'][:20])
            curr_block_hash = hash_bsc_blockdata['result']['parentHash']

        dec_blocks = []
        for dc in latest_blocks:
            dc['blocknumber'] = int(dc['blocknumber'], 16)
            dc['timestamp'] = int(dc['timestamp'], 16)
            dc['size'] = int(dc['size'], 16)
            dc['gasLimit'] = int(dc['gasLimit'], 16)
            dc['gasUsed'] = int(dc['gasUsed'], 16)
            blocknumber.append(dc['blocknumber'])
            timestamp.append(dt.fromtimestamp(dc['timestamp']).strftime('%Y.%m.%d %H:%M:%S'))
            size.append(dc['size'])
            blockhash.append(dc['blockhash'])
            gasLimit.append(dc['gasLimit'])
            gasUsed.append(dc['gasUsed'])
            miner.append(dc['miner'])

            dec_blocks.append(dc)

        df = pd.DataFrame(columns=['blocknumber', 'timestamp', 'size', 'blockhash', 'gasLimit', 'gasUsed', 'miner'])
        df['blocknumber'] = blocknumber
        df['timestamp'] = timestamp
        df['size'] = size
        df['blockhash'] = blockhash
        df['gasLimit'] = gasLimit
        df['gasUsed'] = gasUsed
        df['miner'] = miner

        st.dataframe(df)
        # st.json(dec_blocks)

        transx_blockid = []
        trans_idx = []
        gas = []
        gas_price = []
        from_acct = []
        to_acct = []
        value = []
        type = []

        for i in curr_txs_hash[0]:
            transx_blockid.append(int(i['blockNumber'], 16))
            trans_idx.append(int(i['transactionIndex'], 16))
            gas.append(int(i['gas'], 16))
            gas_price.append(int(i['gasPrice'], 16))
            from_acct.append(i['from'])
            to_acct.append(i['to'])
            value.append(int(i['value'], 16))
            type.append(int(i['type'], 16))

        txdf = pd.DataFrame(
            columns=['transx_blockid', 'trans_idx', 'gas', 'gas_price', 'from_acct', 'to_acct', 'value (WEI)', 'type'])
        txdf['transx_blockid'] = transx_blockid
        txdf['trans_idx'] = trans_idx
        txdf['gas'] = gas
        txdf['gas_price'] = gas_price
        txdf['from_acct'] = from_acct
        txdf['to_acct'] = to_acct
        txdf['value (WEI)'] = value
        txdf['type'] = type

        st.dataframe(txdf)


    if title == "Ripple: XRP":

        # @st.cache_data
        st.subheader("XRP Ledger API")
        st.image("images/ripplesmallimage.png")
        st.write("""Accessing XRP Ledger throuoh Ripple gateway nodes and APIs to the XRP chains, their proprietary network, protocols and each chain's data.""")
        st.write("""**Note:** Data returned from API calls are chain-specific.""")

        XRP_API_URL = "https://s1.ripple.com:51234/"
        xrp_headers = {
            "content-type": "application/json"
        }

        blocknumber = []
        timestamp = []
        block_hash = []
        total_coins = []
        transaction_hash = []

        latest_blocks = []
        latest_tx = []

        init_ledger_hash = "current"
        
        METHOD = "ledger_closed"

        for i in range(0, 1):
            xrp_params = {
                "method": METHOD,
                "params": [
                    {
                        "ledger_index": init_ledger_hash
                    }
                ]
            }
            xrp_data = rq.post(url=XRP_API_URL, json=xrp_params, headers=xrp_headers).json()
            curr_blockhash = xrp_data['result']['ledger_hash']
            curr_blockindex = xrp_data['result']['ledger_index']
            # st.write(xrp_data['result'])

        METHOD = "ledger_data"

        for i in range(0, 20):
            xrp_params = {
                "method": METHOD,
                "params": [
                    {
                        "binary": False,
                        "ledger_hash": curr_blockhash,
                        "limit": 20
                    }
                ]
            }
            xrp_data = rq.post(url=XRP_API_URL, json=xrp_params, headers=xrp_headers).json()
            # st.write(xrp_data['result'])

            blocknumber.append(xrp_data['result']['ledger']['ledger_index'])
            timestamp.append(xrp_data['result']['ledger']['close_time_human'])
            block_hash.append(xrp_data['result']['ledger']['ledger_hash'])
            total_coins.append(xrp_data['result']['ledger']['total_coins'])
            transaction_hash.append(xrp_data['result']['ledger']['transaction_hash'])

            curr_blockhash = xrp_data['result']['ledger']['parent_hash']


        st.write("Latest Ledgers (Blocks)")

        df = pd.DataFrame(columns=['blocknumber', 'timestamp', 'block_hash', 'total_coins', 'transaction_hash'])
        df['blocknumber'] = blocknumber
        df['timestamp'] = timestamp
        df['block_hash'] = block_hash
        df['total_coins'] = total_coins
        df['transaction_hash'] = transaction_hash

        st.dataframe(df)

        # st.write("Latest Transactions")
        
        # latest_tx = []
        # txledger_index = []
        # trans_type = []
        # account = []
        # fee = []
        # expiration = []
        # tx_hash = []

        # METHOD = "ledger_data"

        # xrp_tx_params = {
        #     "method": METHOD,
        #     "params": [
        #         {
        #             "start": 0,
        #             "binary": False,
        #             "limit": 1
        #         }
        #     ]
        # }
        # xrp_tx_data = rq.post(url=XRP_API_URL, json=xrp_tx_params, headers=xrp_headers).json()
        # st.write(xrp_tx_data['result'])

        # latest_tx.append(xrp_tx_data['result']['txs'])

        # for i in range(0, len(latest_tx[0])):
        #     txledger_index.append(latest_tx[0][i]['ledger_index'])
        #     trans_type.append(latest_tx[0][i]['TransactionType'])
        #     account.append(latest_tx[0][i]['Account'])
        #     fee.append(latest_tx[0][i]['Fee'])
        #     #     expiration.append(latest_tx[0][tx]['Expiration'])
        #     tx_hash.append(latest_tx[0][i]['hash'])

        # txdf = pd.DataFrame(columns=['txledger_index', 'trans_type', 'account', 'fee', 'tx_hash'])
        # txdf['txledger_index'] = txledger_index
        # txdf['trans_type'] = trans_type
        # txdf['account'] = account
        # txdf['fee'] = fee
        # # txdf['expiration'] = expiration
        # txdf['tx_hash'] = tx_hash

        # st.dataframe(txdf)