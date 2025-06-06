import streamlit as st

user_name = "User"

prompt = st.chat_input("Say something")
if prompt:
    st.write(f"{user_name}: {prompt}")