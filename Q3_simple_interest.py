import streamlit as st

st.title("Simple Interest Calculator")

p = st.number_input("Enter Principal Amount")
r = st.number_input("Enter Rate of Interest")
t = st.number_input("Enter Time in Years")

if st.button("Calculate"):
    si = (p * r * t) / 100
    st.success(f"Simple Interest is: {si}")
