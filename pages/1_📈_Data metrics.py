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

dfs = {'Set A - Volunteers - Open Eyes': dfA, 'Set B - Volunteers - Closed Eyes': dfB, 'Set C - Patients (epi_zone) - Seizure free': dfC, 'Set D - Patients (Non_epi_zone) - Seizure free': dfD, 'Set E - Patients (epi_zone) - Seizure activity': dfE}

# create a selectbox widget to select the dataframe
selected_df = st.selectbox('Select a set:', list(dfs.keys()),key = 1)
selected_df1 = dfs[selected_df]
column_names = selected_df1.columns.tolist()
selected_column = st.selectbox('Select a column:', column_names)

# Data Quality Metrics
st.header("Data Quality")
st.write("Data Completeness:", dfs[selected_df].count().mean())

#with st.expander(selected_df, expanded=False):
with st.expander('Dataset', expanded=False):
    st.write(dfs[selected_df])

with st.expander('Data Description', expanded=False):
    st.write(dfs[selected_df].describe())

# Data Distribution
st.header("Data Distribution")

fig = px.histogram(dfs[selected_df], x=selected_column, nbins=25)

with st.expander('Histogram', expanded=True):
    st.plotly_chart(fig, use_container_width=True)

fig1 = px.box(dfs[selected_df], x=selected_column)

with st.expander('Box plot', expanded=False):
    st.plotly_chart(fig1, use_container_width=True)

fig2 = px.scatter(dfs[selected_df], x=selected_column, y=selected_df1.columns[1])

with st.expander('Scatter plot', expanded=False):
    st.plotly_chart(fig2, use_container_width=True)

#skewness = stats.skew(dfs[selected_df])
#kurtosis = stats.kurtosis(dfs[selected_df])
#st.write("Skewness:", skewness)
#st.write("Kurtosis:", kurtosis)





