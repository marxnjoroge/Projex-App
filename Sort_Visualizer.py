import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import streamlit.components.v1 as components
import random
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import plotly.graph_objects as go
import plotly.express as px

# # Custom CSS for padding and container alignment
# padding = 1
# st.markdown(f""" 
#     <style>    
#     .reportview-container .main .block-container{{
#         padding-top: {padding}rem;
#         padding-right: {padding}rem;
#         padding-left: {padding}rem;
#         padding-bottom: {padding}rem;
#     }}
#     #MainMenu {{visibility: hidden;}}
#     footer {{visibility: hidden;}}
#     .logo-wrapper {{
#         margin-left: -1rem;
#     }}
#     .main .block-container {{
#         max-width: 1200px;
#         padding-left: 1rem;
#         padding-right: 1rem;
#     }}
#     </style> 
# """, unsafe_allow_html=True)

# # HTML for the animated logo with a function to scale it
# def get_logo_html(scale_percentage=100, background="white"):
#     width = int(400 * scale_percentage / 100)
#     height = int(100 * scale_percentage / 100)
#     font_size = int(46 * scale_percentage / 100)
    
#     return f"""
#     <!DOCTYPE html>
#     <html>
#     <head>
#       <style>
#         .logo-container {{
#           width: {width}px;
#           height: {height}px;
#           position: relative;
#           background: {background};
#           overflow: hidden;
#         }}
        
#         .background-rect {{
#           width: {int(380 * scale_percentage / 100)}px;
#           height: {int(80 * scale_percentage / 100)}px;
#           position: absolute;
#           left: {int(10 * scale_percentage / 100)}px;
#           top: {int(10 * scale_percentage / 100)}px;
#           background: "transparent";
#           overflow: hidden;
#         }}
        
#         .circuit-line {{
#           position: absolute;
#           background: #4299E1;
#           opacity: 0.2;
#         }}
        
#         .horizontal {{
#           height: 1px;
#           width: 100%;
#           animation: glowH 4s infinite;
#         }}
        
#         .vertical {{
#           width: 1px;
#           height: 100%;
#           animation: glowV 4s infinite;
#         }}
        
#         .h1 {{ top: {int(10 * scale_percentage / 100)}px; animation-delay: 0s; }}
#         .h2 {{ top: {int(40 * scale_percentage / 100)}px; animation-delay: 1s; }}
#         .h3 {{ top: {int(70 * scale_percentage / 100)}px; animation-delay: 2s; }}
        
#         .v1 {{ left: {int(40 * scale_percentage / 100)}px; animation-delay: 0.5s; }}
#         .v2 {{ left: {int(140 * scale_percentage / 100)}px; animation-delay: 1.5s; }}
#         .v3 {{ left: {int(240 * scale_percentage / 100)}px; animation-delay: 2.5s; }}
#         .v4 {{ left: {int(340 * scale_percentage / 100)}px; animation-delay: 3.5s; }}
        
#         .text {{
#           position: absolute;
#           left: {int(40 * scale_percentage / 100)}px;
#           top: {int(35 * scale_percentage / 100)}px;
#           font-family: Arial, sans-serif;
#           font-weight: bold;
#           font-size: {font_size}px;
#           z-index: 2;
#         }}
        
#         .text-pro {{
#           color: #AAAAAA;
#           animation: pulse 4s infinite;
#         }}
        
#         .text-jex {{
#           color: #90CDF4;
#           animation: pulse 4s infinite;
#           animation-delay: 2s;
#         }}
        
#         .circle {{
#           width: {int(16 * scale_percentage / 100)}px;
#           height: {int(16 * scale_percentage / 100)}px;
#           position: absolute;
#           top: {int(25 * scale_percentage / 100)}px;
#           border-radius: 50%;
#           z-index: 2;
#         }}
        
#         .circle1 {{
#           right: {int(70 * scale_percentage / 100)}px;
#           background: #90CDF4;
#           animation: pulse 4s infinite;
#         }}
        
#         .circle2 {{
#           right: {int(40 * scale_percentage / 100)}px;
#           background: #AAAAAA;
#           animation: pulse 4s infinite;
#           animation-delay: 2s;
#         }}
        
#         .data-particle {{
#           position: absolute;
#           width: {int(4 * scale_percentage / 100)}px;
#           height: {int(4 * scale_percentage / 100)}px;
#           background: #4299E1;
#           border-radius: 50%;
#           opacity: 0.6;
#           animation: moveParticle 6s infinite linear;
#         }}
        
#         .p1 {{ top: {int(10 * scale_percentage / 100)}px; left: -{int(4 * scale_percentage / 100)}px; animation-delay: 0s; }}
#         .p2 {{ top: {int(40 * scale_percentage / 100)}px; left: -{int(4 * scale_percentage / 100)}px; animation-delay: 2s; }}
#         .p3 {{ top: {int(70 * scale_percentage / 100)}px; left: -{int(4 * scale_percentage / 100)}px; animation-delay: 4s; }}
        
#         @keyframes glowH {{
#           0%, 100% {{ opacity: 0.1; }}
#           50% {{ opacity: 0.3; }}
#         }}
        
#         @keyframes glowV {{
#           0%, 100% {{ opacity: 0.1; }}
#           50% {{ opacity: 0.3; }}
#         }}
        
#         @keyframes pulse {{
#           0%, 100% {{ opacity: 0.8; }}
#           50% {{ opacity: 1; }}
#         }}
        
#         @keyframes moveParticle {{
#           0% {{ transform: translateX(0); }}
#           100% {{ transform: translateX({int(380 * scale_percentage / 100)}px); }}
#         }}
#       </style>
#     </head>
#     <body>
#       <div class="logo-container">
#         <div class="background-rect">
#           <div class="circuit-line horizontal h1"></div>
#           <div class="circuit-line horizontal h2"></div>
#           <div class="circuit-line horizontal h3"></div>
#           <div class="circuit-line vertical v1"></div>
#           <div class="circuit-line vertical v2"></div>
#           <div class="circuit-line vertical v3"></div>
#           <div class="circuit-line vertical v4"></div>
#           <div class="data-particle p1"></div>
#           <div class="data-particle p2"></div>
#           <div class="data-particle p3"></div>
#         </div>
#         <div class="text">
#           <span class="text-pro">PRO</span><span class="text-jex">JEX</span>
#         </div>
#         <div class="circle circle1"></div>
#         <div class="circle circle2"></div>
#       </div>
#     </body>
#     </html>
#     """
# Sidebar setup
sidebar = st.sidebar

# Add scaled-down logo to sidebar with transparent background
# with sidebar:
#   components.html(get_logo_html(scale_percentage=70, background="transparent"), height=87.5)

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

# Sort Vizualizations

# Generate random data
with st.sidebar:
    n = st.slider(label="No. of Array Values", min_value=15, max_value=50,)
data = np.random.randint(1, 100, size=n)

title = st.sidebar.radio(label="Sort Algorithms", options=["Merge", "Quick", "Bubble"])

if title == 'Merge':

    st.subheader(title)

    st.write("This visualization is written in Python using Matplotlib "
                "to both visualize and animate the Sort Algorithm.  A Streamlit "
                "component is then used to dynamically convert the Matplotlib animation "
                "to javascript in order to render it to html.")
    st.write("**Note:** sorting more values takes longer to render.")

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

    components.html(anima.to_jshtml(), height=1000)

if title == 'Quick':
    st.subheader(title)

    st.write("This visualization is written in Python using Matplotlib "
                "to both visualize and animate the Sort Algorithm.  A Streamlit "
                "component is then used to dynamically convert the Matplotlib animation "
                "to javascript in order to render it to html.")
    st.write("**Note:** sorting more values takes longer to render.")
    
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


    