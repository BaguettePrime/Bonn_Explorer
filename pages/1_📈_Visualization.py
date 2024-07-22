import streamlit as st
import pandas as pd
import os
import plotly.express as px

dfA = pd.read_csv("./data/setA.csv")
dfB = pd.read_csv("./data/setB.csv")
dfC = pd.read_csv("./data/setC.csv")
dfD = pd.read_csv("./data/setD.csv")
dfE = pd.read_csv("./data/setE.csv")

# create a dictionary to store the dataframes
dfs = {'DFA': dfA, 'DFB': dfB, 'DFC': dfC, 'DFD': dfD, 'DFE': dfE}

# create a selectbox widget to select the dataframe
selected_df = st.selectbox('Select a dataframe:', list(dfs.keys()),key = 1)

with st.expander(selected_df, expanded=False):
    st.write(dfs[selected_df])
    st.write(dfs[selected_df].describe())

corr_matrix = dfs[selected_df].corr()
st.write(corr_matrix)

# Data Quality Metrics
st.header("Data Quality Metrics")
st.write("Data Completeness:", dfs[selected_df].count().mean())
st.write("Data Accuracy:", dfs[selected_df].accuracy_score())
st.write("Data Consistency:", dfs[selected_df].consistency_score())






