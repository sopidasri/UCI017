import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
import requests
import pandas as pd


dt=pd.read_csv('./data/citrus.csv')

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 300:
        return None
    return r.json()

lottie_url_hello = "https://lottie.host/71e6e18c-2bab-40bd-9121-bd755b60a778/Ib8ewkFcIq.json"
lottie_hello = load_lottieurl(lottie_url_hello)
st_lottie(lottie_hello,key="hello")

html_1 = """
<div style="background-color:#52BE80;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>สถิติข้อมูล Oranges vs. Grapefruit</h5></center>
</div>
"""
st.markdown(html_1, unsafe_allow_html=True)
st.markdown("")

st.subheader("สถิติข้อมูล Oranges vs. Grapefruit")
st.write(dt.head(10))