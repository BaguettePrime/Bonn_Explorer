import streamlit as st
import pandas as pd

# Create a Streamlit app
st.title("🎈 Bonn Explorer")

st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

# Section 1: Data Loading
st.header("Data Loading")

#setA_url = https://raw.githubusercontent.com/BaguettePrime/Bonn_Explorer/main/data/setA.csv
#response = requests.get(url)

df = pd.read_csv("./data/setA.csv")


#df.to_csv('setA.csv', sep=',', index=False, encoding='utf-8')

print(df)
