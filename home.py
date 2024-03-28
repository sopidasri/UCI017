import streamlit as st

st.page_link("Home.py", label="หน้าแรก", icon="🏠")

st.page_link("pages/Statistic.py", label="การนำเสนอข้อมูลด้วยสถิติ", icon="1️⃣")
st.page_link("pages/Chart.py", label="การนำเสนอข้อมูลด้วยการจินตทัศน์ข้อมูล", icon="2️⃣", disabled=False)
st.page_link("http://www.google.com", label="Google", icon="🌎")