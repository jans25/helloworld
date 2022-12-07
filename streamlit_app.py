import streamlit as st
st.set_page_config(layout="wide")

import numpy as np
import altair as alt
import pandas as pd

import streamlit.components.v1 as components
from urllib.request import urlopen


st.header('st.write')




file = open("first_map.html", "r")


HTMLFile = open("first_map.html", "r")
  
# Reading the file
index = HTMLFile.read()

components.html(index, height = 1000)
