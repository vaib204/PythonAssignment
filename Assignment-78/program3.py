import streamlit as st

st.title("Addition Of Two Number")

no1 = st.number_input("Enter Principle Amount:",value = 0,step = 1)
no2 = st.number_input("Enter Rate of Intrest:",value = 0,step = 1)
no3 = st.number_input("Enter Time Period:",value = 0,step = 1)

if st.button("Calculate"):
  result = no1 * no2 * no3 /100

  st.success("Intrest is:"+str(result))