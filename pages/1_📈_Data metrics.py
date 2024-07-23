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

# Data Quality Metrics
st.header("Data Quality")
st.write("Data Completeness:", dfs[selected_df].count().mean())

with st.expander(selected_df, expanded=True):
    st.write(dfs[selected_df])

st.write(dfs[selected_df].describe())

# Data Distribution
st.header("Data Distribution")
fig = px.histogram(dfs[selected_df], x=dfs[selected_df].columns[0], nbins=25)
st.plotly_chart(fig, use_container_width=True)

# Calculate metrics
skewness = stats.skew(dfs[selected_df])
kurtosis = stats.kurtosis(dfs[selected_df])

# Display metrics
st.write("Skewness:", skewness)
st.write("Kurtosis:", kurtosis)





