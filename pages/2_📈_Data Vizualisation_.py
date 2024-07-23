import streamlit as st
import pandas as pd
import os
import plotly.express as px
import numpy as np
from scipy import stats

# Generate an array of timestamps

sf= 173.86
x = 23.6
timestamps = np.arange(0, x, 1/sf)

st.header("Data Vizualisation")

dfA = pd.read_csv("./data/setA.csv")
dfB = pd.read_csv("./data/setB.csv")
dfC = pd.read_csv("./data/setC.csv")
dfD = pd.read_csv("./data/setD.csv")
dfE = pd.read_csv("./data/setE.csv")

# create a dictionary to store the dataframes
dfs = {'DFA': dfA, 'DFB': dfB, 'DFC': dfC, 'DFD': dfD, 'DFE': dfE}

# create a selectbox widget to select the dataframe
selected_df = st.selectbox('Select a dataframe:', list(dfs.keys()),key = 1)
selected_df1 = dfs[selected_df]
column_names = selected_df1.columns.tolist()
selected_column = st.selectbox('Select a column:', column_names)





# create a figure using plotly express
fig = px.line(selected_df1, x=timestamps, y=selected_column)
#fig = px.line(selected_df1, x=selected_df1.index, y=selected_column)
# This styles the line
fig.update_traces(line=dict(width=1.0))

# display the figure
st.plotly_chart(fig, use_container_width=True)

