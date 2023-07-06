import streamlit as st
import pandas as pd


code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')


