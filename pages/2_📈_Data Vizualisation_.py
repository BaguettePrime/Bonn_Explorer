import streamlit as st
import pandas as pd
import os
import plotly.express as px
import numpy as np
from scipy import stats

# Generate an array of timestamps

x = 4097  # number of datapoints
sf = 173.61  # sampling frequency

# Calculate the total duration in seconds
duration = x / sf

# Generate an array of timestamps
timestamps = np.arange(0, duration, 1/sf)

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
fig = px.line(selected_df1, x=timestamps, y=selected_column, 
              title='Time Series Data')
#fig = px.line(selected_df1, x=selected_df1.index, y=selected_column)
# This styles the line
fig.update_traces(line=dict(width=1.0))
fig.update_layout(xaxis_title='Time (s)', yaxis_title="Amplitude")

# display the figure
st.plotly_chart(fig, use_container_width=True)

# compute the FFT of the selected time series
fft_values = np.fft.fft(selected_df1[selected_column].values)
fft_frequencies = np.fft.fftfreq(len(selected_df1[selected_column].values), d=1/sf)

# create a figure using plotly express for the FFT
fft_fig = px.line(x=fft_frequencies, y=np.abs(fft_values))
fft_fig.update_layout(title='FFT of the Time Series Data',
                      xaxis_title='Frequency (Hz)',
                      yaxis_title='Amplitude',xaxis=dict(range=[0, 55])) 
fft_fig.update_traces(line=dict(width=1.0),line_color = 'red')
                      

# display the FFT figure
st.plotly_chart(fft_fig, use_container_width=True)

