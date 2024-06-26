import pandas as pd
import streamlit as st
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score,mean_squared_error
st.image('./pic/stock1.jpg')
st.title("การพยากรณ์ข้อมูลด้วยเทคนิค Linear Regression")
st.subheader("การพยากรณ์ข้อมูล stock index price")

df=pd.read_csv('./data/stock_index_price.csv')
st.write(df.head(10))

#st.line_chart(df)
#st.line_chart(df, x="interest_rate", y="unemployment_rate", color="stock_index_price")
st.image('./pic/stock2.jpg')
st.subheader("กราฟแสดงข้อมูล stock index price")
st.line_chart(
   df, x="interest_rate", y=["stock_index_price"], color=["#FF0000"]  # Optional
)

x=df[['interest_rate','unemployment_rate']]
y=df['stock_index_price']
pf=PolynomialFeatures(degree=3)
x_poly=pf.fit_transform(x)

x_train,x_test,y_train,y_test =train_test_split(x_poly,y,random_state=0)

modelRegress=LinearRegression()
modelRegress.fit(x_train,y_train)
x1=st.number_input("กรุณาป้อนข้อมูล interest_rate:")
x2=st.number_input("กรุณาป้อนข้อมูล unemployment_rate:")

html_1 = """
<div style="background-color:#76D7C4;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h4>การพยากรณ์ข้อมูล stock index price ด้วยเทคนิค 
<br>Linear Regression</h4></center>
</div>
"""
st.markdown(html_1, unsafe_allow_html=True)
st.markdown("")
st.image('./pic/stock3.jpg')

if st.button("พยากรณ์ข้อมูล"):
    x_input=[[x1,x2]]
    y_predict=modelRegress.predict(pf.fit_transform(x_input))
    st.write(y_predict)
    st.button("ไม่พยากรณ์ข้อมูล")
else:
    st.button("ไม่พยากรณ์ข้อมูล")