import streamlit as st
st.title("Welcome to my frist app")
st.write("Hello")
name = st.text_input("Enter your name...")
if st.button("submit"):
st.write("Hello", name)