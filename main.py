import streamlit as st
import pandas as pd
import requests as rq
import streamlit.components.v1 as components
from datetime import datetime as dt, timedelta

st.set_page_config(page_title=None, page_icon=None, layout="centered", initial_sidebar_state="auto", menu_items=None)

# Page configuration
st.title = "Projex"

# Custom CSS for padding and container alignment
padding = 1
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
    .logo-wrapper {{
        margin-left: -1rem;
    }}
    .main .block-container {{
        max-width: 1200px;
        padding-left: 1rem;
        padding-right: 1rem;
    }}
    </style> 
""", unsafe_allow_html=True)

# HTML for the animated logo with a function to scale it
def get_logo_html(scale_percentage=100, background="transparent"):
    width = int(400 * scale_percentage / 100)
    height = int(100 * scale_percentage / 100)
    font_size = int(46 * scale_percentage / 100)
    
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


# Create a container for better alignment control
st.markdown('<div class="logo-wrapper">', unsafe_allow_html=True)
# Render the full-size animated logo
components.html(get_logo_html(scale_percentage=100), height=120)
st.write("---")
st.markdown('</div>', unsafe_allow_html=True)

# Sidebar setup
sidebar = st.sidebar

# Add scaled-down logo to sidebar with transparent background
with sidebar:
  components.html(get_logo_html(scale_percentage=40, background="transparent"), height=48)
  
Projex = st.Page("Projex.py", title="Projex", default = True)
AI_Assistant = st.Page("AI_Assistant.py", title="AI Assistant")
Blockchain_Explorer = st.Page("Blockchain_Explorer.py", title = "Blockchain Explorer")
Sort_Visualizer = st.Page("Sort_Visualizer.py", title = "Sort Visualizer")

pg = st.navigation(
      {
        "Main": [Projex],
        "Tools": [AI_Assistant, Blockchain_Explorer, Sort_Visualizer],       
      }
    )

pg.run()

with sidebar:
   st.write("---")
   st.caption("Marx Njoroge.2024")