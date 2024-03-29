import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
import requests

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url_hello = "https://lottie.host/92c3dfeb-937f-44be-8aef-dc6480e2b4e8/uRdHEL97X0.json"
lottie_hello = load_lottieurl(lottie_url_hello)
st_lottie(lottie_hello,key="hello")

st.page_link("home.py", label="หน้าแรก", icon="🏠")

st.page_link("pages/1🧮Statistic.py", label="การนำเสนอข้อมูลด้วยสถิติ", icon="1️⃣")
st.page_link("pages/2📊Chart.py", label="การนำเสนอข้อมูลด้วยการจินตทัศน์ข้อมูล", icon="2️⃣", disabled=False)
st.page_link("pages/3🎡KNNClassify.py", label="การจำแนกข้อมูลด้วยเทคนิค K-NN", icon="3️⃣", disabled=False)
st.page_link("pages/4🏝️DecisionTreeClassify.py", label="การจำแนกข้อมูลด้วยเทคนิคDecisionTree", icon="4️⃣", disabled=False)
st.page_link("pages/5🥗NaivebayeClassify.py", label="การจำแนกข้อมูลด้วยเทคนิคNaiveBayes", icon="5️⃣", disabled=False)
st.page_link("pages/6📈RegressionPrediction.py", label="การพยากรณ์ข้อมูลด้วยเทคนิคRegression", icon="6️⃣", disabled=False)

st.page_link("http://www.google.com", label="Google", icon="🌎")