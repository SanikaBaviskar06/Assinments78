
import streamlit as st

st.title("Even or Odd Number")

num = st.number_input("Enter an Integer", step=1)

if st.button("Check"):
    if num % 2 == 0:
        st.success(" Number is Even")
    else:
        st.success(" Number is Odd")
