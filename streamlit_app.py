import streamlit as st
import pandas as pd
import os
import plotly.express as px

st.set_page_config(
        page_title="🧠 Bonn Explorer",
)

st.title("🧠 Welcome to the Bonn Explorer")

st.write("""
Let's start exploring! 
Everything you need is (almost) here: [docs.streamlit.io](https://docs.streamlit.io/).
""")

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

The EEG signals were recorded using a 128-channel EEG system, but only a single channel is provided in the dataset. 
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

st.write('Band-pass filter settings were 0.53–40 Hz ~12 dB/oct.!. SF 173.61')

st.header("Dataset description")
st.image('data/Table.png', caption='Technical summary')

