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

# Sidebar setup
sidebar = st.sidebar

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

    with st.status("Loading", expanded=True, state='running'):

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
    
    with st.status("Loading", expanded=True, state='running'):

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

    with st.status("Loading", expanded=True, state='running'):

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


    