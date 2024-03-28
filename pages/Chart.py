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

html_1 = """
<div style="background-color:#52BE80;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>สถิติข้อมูล Oranges vs. Grapefruit</h5></center>
</div>
"""
st.markdown(html_1, unsafe_allow_html=True)
st.markdown("")


st.write('ผลรวม')
cl1,cl2,cl3,cl4,cl5=st.columns(5)
cl1.write(dt['diameter'].sum())
cl2.write(dt['weight'].sum())
cl3.write(dt['red'].sum())
cl4.write(dt['green'].sum())
cl5.write(dt['blue'].sum())

st.write("กราฟแท่ง")
a=dt['diameter'].sum()
b=dt['weight'].sum()
c=dt['red'].sum()
d=dt['green'].sum()
e=dt['blue'].sum()
dx=[a,b,c,d,e]
cx=pd.DataFrame(dx,index=["diameter", "weight", "red","green","blue"])
st.bar_chart(cx)

st.write('ค่าเฉลี่ย')
cl11,cl12,cl13,cl14,cl15=st.columns(5)
cl11.write(dt['diameter'].mean())
cl12.write(dt['weight'].mean())
cl13.write(dt['red'].mean())
cl14.write(dt['green'].mean())
cl15.write(dt['blue'].mean())

st.write("Area_Chart")
a=dt['diameter'].mean()
b=dt['weight'].mean()
c=dt['red'].mean()
d=dt['green'].mean()
e=dt['blue'].mean()
dxt=[a,b,c,d,e]
cxx=pd.DataFrame(dxt,index=["diameter", "weight", "red","green","blue"])
st.area_chart(cxx)

labels = ['diameter', 'weight','red','green','blue']
sizes = [20,20,10,20,30]
explode = (0, 0.1,0,0,0) 
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
st.pyplot(fig1)
