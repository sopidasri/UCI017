import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
import requests
import pandas as pd


dt=pd.read_csv('./data/citrus.csv')

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url_hello = "https://lottie.host/71e6e18c-2bab-40bd-9121-bd755b60a778/Ib8ewkFcIq.json"
lottie_hello = load_lottieurl(lottie_url_hello)
st_lottie(lottie_hello,key="hello")

st.subheader("การนำเสนอข้อมูลด้วยการจินตทัศน์ข้อมูล")

st.write("Area_Chart")
a=dt['diameter'].mean()
b=dt['weight'].mean()
c=dt['red'].mean()
d=dt['green'].mean()
e=dt['blue'].mean()
dxt=[a,b,c,d]
cxx=pd.DataFrame(dxt,index=["diameter", "weight", "red","green","blue"])
st.area_chart(cxx)