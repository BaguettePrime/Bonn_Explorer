import streamlit as st
import pandas as pd
import os
import plotly.express as px

# Create a Streamlit app
st.title("🎈 Bonn Explorer")

st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

# Section 1: Introduction
st.header("Welcome to the Bonn Explorer")

st.write("""
The Bonn dataset is a popular benchmark dataset for EEG-based seizure detection and epilepsy diagnosis. 
It was introduced in 2001 by Ralph Andrzejak and colleagues from the University of Bonn, Germany.

This app is designed to explore the Bonn dataset, visualize the EEG signals, extract features, and train a classifier for seizure detection.

In this app, you can:
* Explore the dataset and visualize the EEG signals
* Extract features from the EEG signals
* Train a classifier for seizure detection
* Evaluate the performance of the classifier

Let's get started!
""")

# Add a button to navigate to the next page
if st.button("Explore the Dataset"):
    # Navigate to the next page
    st.write("You can now explore the dataset!")
    # Add a link to the next page (e.g., a page to select the dataset)
    st.markdown("[Select a dataset](page2)")


# Section 1: Data Loading
st.header("Dataset inspection and description")

#setA_url = https://raw.githubusercontent.com/BaguettePrime/Bonn_Explorer/main/data/setA.csv
#response = requests.get(url)



dfA = pd.read_csv("./data/setA.csv")
dfB = pd.read_csv("./data/setB.csv")
dfC = pd.read_csv("./data/setC.csv")
dfD = pd.read_csv("./data/setD.csv")
dfE = pd.read_csv("./data/setE.csv")

# create a dictionary to store the dataframes
dfs = {'DFA': dfA, 'DFB': dfB, 'DFC': dfC, 'DFD': dfD, 'DFE': dfE}

#df.to_csv('setA.csv', sep=',', index=False, encoding='utf-8')
#st.dataframe(df)
#print(df)
# create a selectbox widget to select the dataframe
selected_df = st.selectbox('Select a dataframe:', list(dfs.keys()),key = 1)

with st.expander(selected_df, expanded=False):
    st.write(dfs[selected_df])


#st.dataframe(selected_df)

# Section 1: Data Vizualisation
st.header("Data Vizualisation")
# create a selectbox widget to select the dataframe
#@st.cache_data
selected_df1 = st.selectbox('Select a dataframe:', list(dfs.keys()),key = 2)
selected_df2 = dfs[selected_df1]



# create a selectbox widget to select the column
column_names = selected_df2.columns.tolist()
selected_column = st.selectbox('Select a column:', column_names)

# create a figure using plotly express
fig = px.line(selected_df2, x=selected_df2.index, y=selected_column)

# display the figure
st.plotly_chart(fig, use_container_width=True)

