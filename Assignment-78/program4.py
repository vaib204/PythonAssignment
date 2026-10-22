import streamlit as st

name = st.text_input("Enter Student Name:")

Marks1 = st.number_input("Enter Java Marks:",value = 0,step = 1)
Marks2 = st.number_input("Enter Python Marks:",value = 0,step = 1)
Marks3 = st.number_input("Enter C Marks:",value = 0,step = 1)

if st.button("Calcualte"):
  total = 100

  Marks1_Percen = Marks1/total *100
  st.write("Percentage of java:"+str(Marks1_Percen))
  Marks2_Percen = Marks2/total *100
  st.write("Percentage of Python:"+str(Marks2_Percen))
  Marks3_Percen = Marks3/total *100
  st.write("Percentage of C:"+str(Marks3_Percen))

  if Marks1 > 40:
    st.success("Passed Java Exam")
  else:
    st.error("Failed java Exam ")
  if Marks2 > 40:
      st.success("Passed python exam")
  else:
      st.error("Failed python exam")
  if Marks3 > 40:
      st.success("Passed c exam")
  else:
      st.error("Failed c exam")      
      
  