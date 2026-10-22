import streamlit as st

st.title("Student Result Calculator")

name = st.text_input("Enter Student Name")

sub1 = st.number_input(
    "Enter Subject 1 Marks",
    min_value=0,
    max_value=100,
    step=1
)

sub2 = st.number_input(
    "Enter Subject 2 Marks",
    min_value=0,
    max_value=100,
    step=1
)

sub3 = st.number_input(
    "Enter Subject 3 Marks",
    min_value=0,
    max_value=100,
    step=1
)

if st.button("Calculate Result"):

    total = sub1 + sub2 + sub3
    percentage = total / 3

    st.write("Student Name:", name)
    st.write("Total Marks:", total, "/ 300")
    st.write("Percentage:", percentage, "%")

    if sub1 >= 40 and sub2 >= 40 and sub3 >= 40:
        st.success("Result: PASS")
    else:
        st.error("Result: FAIL")
