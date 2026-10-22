import streamlit as st

st.title("Check Even Or Odd")

no1 = st.number_input("Enter First Number:",value = 0,step = 1)

if st.button("Even/Odd"):
  if no1 % 2 == 0:
    st.write("Even")
  else:
    st.write("Odd")
 