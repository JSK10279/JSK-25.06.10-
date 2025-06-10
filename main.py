import streamlit as st
st.title("나의 첫 app")
st.write("hello")
name=st.text_imput("이름입력")
if name:
  if name=="JSK":
    st.success("반갑습니다")
  else:
    st.warning("지정되지 않은 사용자입니다")
