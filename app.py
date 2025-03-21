import streamlit as st
import requests
st.title("contact form")

name=st.text_input("Name")
email=st.text_input("Email")
message=st.text_area("message")

if st.button('Submit'):
    data={
        "name":name,
        "email":email,
        "message":message 
    }
    response=requests.post('http://127.0.0.1:8000//submit_form',json=data)

    if response.status_code==200:
        st.success("Form submitted successfully")
    else:
        st.error("something went wrong")