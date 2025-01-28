import streamlit as st
import pandas as pd
import requests as rq
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import streamlit.components.v1 as components
from datetime import datetime as dt, timedelta

# Page configuration
st.set_page_config(layout="wide", page_title="Projex")

# Custom CSS for padding
padding = 3
st.markdown(f""" 
    <style>    
    .reportview-container .main .block-container{{
        padding-top: {padding}rem;
        padding-right: {padding}rem;
        padding-left: {padding}rem;
        padding-bottom: {padding}rem;
    }}
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    </style> 
""", unsafe_allow_html=True)

# HTML for the animated logo with a function to scale it
def get_logo_html(scale_percentage=100, background="white"):
    width = int(400 * scale_percentage / 100)
    height = int(100 * scale_percentage / 100)
    font_size = int(42 * scale_percentage / 100)
    
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
      <style>
        .logo-container {{
          width: {width}px;
          height: {height}px;
          position: relative;
          background: {background};
          overflow: hidden;
        }}
        
        .background-rect {{
          width: {int(380 * scale_percentage / 100)}px;
          height: {int(80 * scale_percentage / 100)}px;
          position: absolute;
          left: {int(10 * scale_percentage / 100)}px;
          top: {int(10 * scale_percentage / 100)}px;
          background: "transparent";
          overflow: hidden;
        }}
        
        .circuit-line {{
          position: absolute;
          background: #4299E1;
          opacity: 0.2;
        }}
        
        .horizontal {{
          height: 1px;
          width: 100%;
          animation: glowH 4s infinite;
        }}
        
        .vertical {{
          width: 1px;
          height: 100%;
          animation: glowV 4s infinite;
        }}
        
        .h1 {{ top: {int(10 * scale_percentage / 100)}px; animation-delay: 0s; }}
        .h2 {{ top: {int(40 * scale_percentage / 100)}px; animation-delay: 1s; }}
        .h3 {{ top: {int(70 * scale_percentage / 100)}px; animation-delay: 2s; }}
        
        .v1 {{ left: {int(40 * scale_percentage / 100)}px; animation-delay: 0.5s; }}
        .v2 {{ left: {int(140 * scale_percentage / 100)}px; animation-delay: 1.5s; }}
        .v3 {{ left: {int(240 * scale_percentage / 100)}px; animation-delay: 2.5s; }}
        .v4 {{ left: {int(340 * scale_percentage / 100)}px; animation-delay: 3.5s; }}
        
        .text {{
          position: absolute;
          left: {int(40 * scale_percentage / 100)}px;
          top: {int(35 * scale_percentage / 100)}px;
          font-family: Arial, sans-serif;
          font-weight: bold;
          font-size: {font_size}px;
          z-index: 2;
        }}
        
        .text-pro {{
          color: #AAAAAA;
          animation: pulse 4s infinite;
        }}
        
        .text-jex {{
          color: #90CDF4;
          animation: pulse 4s infinite;
          animation-delay: 2s;
        }}
        
        .circle {{
          width: {int(16 * scale_percentage / 100)}px;
          height: {int(16 * scale_percentage / 100)}px;
          position: absolute;
          top: {int(25 * scale_percentage / 100)}px;
          border-radius: 50%;
          z-index: 2;
        }}
        
        .circle1 {{
          right: {int(70 * scale_percentage / 100)}px;
          background: #90CDF4;
          animation: pulse 4s infinite;
        }}
        
        .circle2 {{
          right: {int(40 * scale_percentage / 100)}px;
          background: #AAAAAA;
          animation: pulse 4s infinite;
          animation-delay: 2s;
        }}
        
        .data-particle {{
          position: absolute;
          width: {int(4 * scale_percentage / 100)}px;
          height: {int(4 * scale_percentage / 100)}px;
          background: #4299E1;
          border-radius: 50%;
          opacity: 0.6;
          animation: moveParticle 6s infinite linear;
        }}
        
        .p1 {{ top: {int(10 * scale_percentage / 100)}px; left: -{int(4 * scale_percentage / 100)}px; animation-delay: 0s; }}
        .p2 {{ top: {int(40 * scale_percentage / 100)}px; left: -{int(4 * scale_percentage / 100)}px; animation-delay: 2s; }}
        .p3 {{ top: {int(70 * scale_percentage / 100)}px; left: -{int(4 * scale_percentage / 100)}px; animation-delay: 4s; }}
        
        @keyframes glowH {{
          0%, 100% {{ opacity: 0.1; }}
          50% {{ opacity: 0.3; }}
        }}
        
        @keyframes glowV {{
          0%, 100% {{ opacity: 0.1; }}
          50% {{ opacity: 0.3; }}
        }}
        
        @keyframes pulse {{
          0%, 100% {{ opacity: 0.8; }}
          50% {{ opacity: 1; }}
        }}
        
        @keyframes moveParticle {{
          0% {{ transform: translateX(0); }}
          100% {{ transform: translateX({int(380 * scale_percentage / 100)}px); }}
        }}
      </style>
    </head>
    <body>
      <div class="logo-container">
        <div class="background-rect">
          <div class="circuit-line horizontal h1"></div>
          <div class="circuit-line horizontal h2"></div>
          <div class="circuit-line horizontal h3"></div>
          <div class="circuit-line vertical v1"></div>
          <div class="circuit-line vertical v2"></div>
          <div class="circuit-line vertical v3"></div>
          <div class="circuit-line vertical v4"></div>
          <div class="data-particle p1"></div>
          <div class="data-particle p2"></div>
          <div class="data-particle p3"></div>
        </div>
        <div class="text">
          <span class="text-pro">PRO</span><span class="text-jex">JEX</span>
        </div>
        <div class="circle circle1"></div>
        <div class="circle circle2"></div>
      </div>
    </body>
    </html>
    """

# Sidebar setup
sidebar = st.sidebar

# Add scaled-down logo to sidebar with transparent background
sidebar.markdown("<div style='margin-bottom: 20px;'>", unsafe_allow_html=True)
with sidebar:
  components.html(get_logo_html(scale_percentage=70, background="transparent"), height=87.5)
sidebar.markdown("</div>", unsafe_allow_html=True)

# Sidebar content
sidebar.header("Python Projects \n(Press 'r' or 'R' to refresh)")
option = sidebar.selectbox("Tools", ('Projex', 'AI Assistant', 'Blockchain Explorer', 'Sort Visualizations'))

# Main content
if option == 'Projex':
    # Render the full-size animated logo
    components.html(get_logo_html(scale_percentage=100), height=120)
    
    st.write("Welcome to Projex, a platform showcasing innovative projects that push the boundaries of technology and innovation. As hiring managers, you're likely looking for talented individuals who can bring cutting-edge skills and expertise to your team. This project website is designed to give you a glimpse into the exciting work being done by our developers, and to help you identify top talent who can drive your organization forward.")
    
    st.write("On this website, you'll find three distinct projects that demonstrate our team's capabilities in various areas of technology:")

    st.markdown("### Blockchain Explorer")
    st.write("The Blockchain Explorer is a comprehensive platform for exploring and analyzing blockchain transactions, providing insights into network activity, transaction patterns, and more. This project showcases our team's expertise in blockchain development, data analysis, and visualization.")

    st.markdown("### Large Language Model")
    st.write("This Large Language Model wrapper is an AI application that leverages the power of machine learning to analyze and generate human-like text. This project highlights our team's skills in natural language processing, machine learning, and software development.")

    st.markdown("### Sort Visualizer")
    st.write("This Sort Visualizer is an interactive web application that illustrates the process of sorting algorithms, providing a visual representation of complex data structures and algorithmic processes. This project demonstrates our team's ability to design and develop engaging user interfaces, as well as their understanding of computer science concepts.")

    st.write("By exploring these projects, you'll gain a deeper understanding of our team's capabilities and expertise in areas such as blockchain development, AI, machine learning, and software engineering. Whether you're looking to fill a specific role or seeking to bring in a team of talented developers, we believe that our projects will give you a compelling reason to consider our team for your organization's needs.")

    st.write("I am excited for feature updates to these projects and look forward to the opportunity to collaborate on upcoming projects.")

elif option == 'AI Assistant':
    st.header("AI Assistant")
    st.write("AI Assistant content goes here...")

elif option == 'Blockchain Explorer':
    st.header("Blockchain Explorer")
    st.write("Blockchain Explorer content goes here...")

elif option == 'Sort Visualizations':
    st.header("Sort Visualizations")
    st.write("Sort Visualizations content goes here...")
