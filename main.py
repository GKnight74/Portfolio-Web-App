import streamlit as st

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("George Knight")
    content = """ Hi, I am George! I am a beginner Python programmer and Technical Writer. \n
    I am from Texas and am enjoying my coding experience so far."""
    st.info(content)