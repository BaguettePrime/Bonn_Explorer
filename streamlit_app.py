import streamlit as st
import pandas as pd
import os
import plotly.express as px

# Create a Streamlit app
st.set_page_config(
        page_title="🧠 Bonn Explorer",
)

st.title("🧠 Welcome to the Bonn Explorer")

st.write("""
Let's start exploring! 
Everything you need is (almost) here: [docs.streamlit.io](https://docs.streamlit.io/).
""")

# Section 1: Introduction
#st.header("Welcome to the Bonn Explorer")

st.write("""
The Bonn dataset has become a standard benchmark in the field of EEG analysis and seizure detection, allowing researchers to compare different methods and algorithms on a common ground.
It was introduced in 2001 by Ralph Andrzejak and colleagues from the University of Bonn, Germany.

**Dataset Overview**

The Bonn dataset consists of 5 sets (A-E) of EEG recordings, each containing 100 single-channel EEG segments of 23.6 seconds duration. 
The recordings were obtained from 5 different groups:

* **Set A**: Volunteers relaxed in an awake state with eyes open from surface electrodes
* **Set B**: Volunteers relaxed in an awake state with eyes closed from surface electrodes
* **Set C**: Epileptic patients during seizure free intervals from the hippocampal formation of the opposite hemisphere of the brain
* **Set D**: Epileptic patients during seizure free intervals from within the epileptogenic zone
* **Set E**: pileptic patients during seizure activity (segments were selected from all recording sites exhibiting ictal activity)

The EEG signals were recorded using a 128-channel EEG system, but only a single channel (the Cz electrode) is provided in the dataset. 
The sampling rate is 173.61 Hz.

For more information about the Bonn dataset, please refer to the [original paper](https://www.upf.edu/documents/229517819/232450661/Andrzejak-PhysicalReviewE2001.pdf/0e9a54b8-8993-b400-743e-4d64fa29fb63) by Andrzejak et al.

Bonn dataset download [page](https://www.upf.edu/web/ntsa/downloads/-/asset_publisher/xvT6E4pczrBw/content/2001-indications-of-nonlinear-deterministic-and-finite-dimensional-structures-in-time-series-of-brain-electrical-activity-dependence-on-recording-regi) 

**App Overview**

This app is designed to explore the Bonn dataset, visualize the EEG signals, extract features, and train a classifier for seizure detection.

In this app, you can:
* Explore the dataset and visualize the EEG signals
* Extract features from the EEG signals

In this app, you will wait for the next update to:
* Train a classifier for seizure detection
* Evaluate the performance of the classifier

Let's get started!
""")

# Add a button to navigate to the next page
#if st.button("Explore the Dataset"):
    # Navigate to the next page
 #   st.write("You can now explore the dataset!")
    # Add a link to the next page (e.g., a page to select the dataset)
  #  st.markdown("[Select a dataset](page2)")
st.write('Band-pass filter settings were 0.53–40 Hz ~12 dB/oct.!. SF 173.61')

st.header("Dataset description")

dfA = pd.read_csv("./data/setA.csv")
dfB = pd.read_csv("./data/setB.csv")
dfC = pd.read_csv("./data/setC.csv")
dfD = pd.read_csv("./data/setD.csv")
dfE = pd.read_csv("./data/setE.csv")

# create a dictionary to store the dataframes
dfs = {'Set A': dfA, 'Set B': dfB, 'Set C': dfC, 'Set D': dfD, 'Set E': dfE}
dfset = {'Set A': 'Volunteers - Open Eyes', 'Set B': 'Volunteers - Closed Eyes', 'Set C': 'Patients(epi_zone) - Seizure free', 'Set D': 'Patients(Non_epi_zone) - Seizure free', 'Set E': 'Patients(epi_zone) - Seizure activity'}

st.image('data/Table.png', caption='Technical summary')

