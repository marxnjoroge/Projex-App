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
