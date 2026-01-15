import streamlit as st
import pandas as pd

st.title("favorite things")

if "names" not in st.session_state:
  st.session_state.names = {
    "Ivan": 0,
    "Georgi": 0,
    "Rado": 0,
    "Daniel": 0
  }
if "grade" not in st.session_state:
  st.session_state.grade = {
    "6": 0,
    "5": 0,
    "4": 0,
    "3": 0,
    "2": 0
  }
st.subheader("pick grade for student")
name = st.selectbox("student: ", list(st.session_state.names.keys()))
num = st.selectbox("grade: ", list(st.session_state.grade.keys()))

if st.button("save choice"):
  st.session_state.names[name] += 1
  st.session_state.grade[num] += 1
  st.success("saved")
st.divider()
st.subheader("grades")
st.write("graded students")
names_df = pd.DataFrame.from_dict(
  st.session_state.names, orient="index", columns=["amount"]
)
st.bar_chart(names_df)

st.write("grades")
grades_df = pd.DataFrame.from_dict(
  st.session_state.grade, orient="index", columns=["amount"]
)
st.bar_chart(grades_df)
