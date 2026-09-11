# 파이참 내부 터미널에서 pip install streamlit
import streamlit as st
# streamlit hello -> 종료는 Ctrl+C

st.title('anything')
st.write('something')
# streamlit run main02.py

n = st.text_input('name : ')
st.write(f'{n} Nice to meet you')