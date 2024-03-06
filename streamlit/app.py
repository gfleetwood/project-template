import streamlit as st
import pandas as pd
import requests
from time import sleep
from os import environ

st.set_page_config(layout = 'wide')
st.title("App")    
query = st.text_input("Enter Term to Search For")

df = get_df()

if "df" not in st.session_state: 
  st.session_state["df"] = df

query = st.text_input("Enter term to search for")

if query:
    mask = df.applymap(lambda x: query in str(x).lower()).any(axis = 1)
    df = df[mask]

st.data_editor(df, hide_index = True)

while True:
  # 20 minutes
  time.sleep(60*20)
  st.rerun()
