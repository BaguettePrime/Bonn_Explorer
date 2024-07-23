import streamlit as st
import pandas as pd
import os
import plotly.express as px
import numpy as np
from scipy import stats


dfA = pd.read_csv("./data/setA.csv")
dfB = pd.read_csv("./data/setB.csv")
dfC = pd.read_csv("./data/setC.csv")
dfD = pd.read_csv("./data/setD.csv")
dfE = pd.read_csv("./data/setE.csv")

# create a dictionary to store the dataframes
dfs = {'DFA': dfA, 'DFB': dfB, 'DFC': dfC, 'DFD': dfD, 'DFE': dfE}

# create a selectbox widget to select the dataframe
selected_df = st.selectbox('Select a dataframe:', list(dfs.keys()),key = 1)
column_names = selected_df.columns.tolist()
selected_column = st.selectbox('Select a column:', column_names)





# create a figure using plotly express
fig = px.line(selected_df, x=selected_df.index, y=selected_column)

# display the figure
st.plotly_chart(fig, use_container_width=True)

