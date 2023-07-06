import streamlit as st
import pandas as pd

st.write(""" # My first app
         Hello *World!*   """)


df = pd.read_csv("mydata.csv")
st.line_chart(df)