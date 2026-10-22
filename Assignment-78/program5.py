import streamlit as st

st.title("Check Fahrenheit")

no1 = st.number_input("Enter Temprature:",value = 0,step = 1)

if st.button("Convert"):
  F = (no1 * 9/5 )+ 32
  st.success("Fahrenheit Conversion:"+str(F))