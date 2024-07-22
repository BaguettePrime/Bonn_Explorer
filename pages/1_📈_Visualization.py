import streamlit as st
import pandas as pd
import os
import plotly.express as px

# create a selectbox widget to select the dataframe
selected_df = st.selectbox('Select a dataframe:', list(dfs.keys()),key = 1)

with st.expander(selected_df, expanded=False):
    st.write(dfs[selected_df])

