import streamlit as st
import pandas as pd
import os

# Create a Streamlit app
st.title("🎈 Bonn Explorer")

st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

# Section 1: Data Loading
st.header("Data Loading")

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
selected_df = st.selectbox('Select a dataframe:', list(dfs.keys()))

with st.expander(selected_df, expanded=False):
    st.write(dfs[selected_df])


#st.dataframe(selected_df)

# Section 1: Data Vizualisation
st.header("Data Vizualisation")
