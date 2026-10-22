
import streamlit as st

st.title("Addition of Two Numbers")

num1 = st.number_input("Enter First Number")
num2 = st.number_input("Enter Second Number")

if st.button("Add"):
    result = num1 + num2
    st.success(f"Addition is: {result}")
