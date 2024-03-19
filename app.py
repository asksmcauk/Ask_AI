import streamlit as st
import json
import requests

st.set_page_config(page_title="web site health check",page_icon=":tada:",layout="wide")
st.subheader("Hi, Please upload json file to check the health status of your website")

#https://discuss.streamlit.io/t/using-an-api-from-inside-streamlit-app/37477/22?page=2

uploaded_file = st.file_uploader("Choose a file", type=["json"])
is_submit = st.button('Process File')
if is_submit and uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    try:
        st.write("Uploaded FIle name is : ",uploaded_file.name)
       # with open(uploaded_file.name, 'rb') as f:
            #r = requests.post(
                #'https://websitemonitorapp.azurewebsites.net/websitestatus',
                #files={uploaded_file.name: bytes_data})
        r = requests.post(
            'https://websitemonitorapp.azurewebsites.net/websitestatus',
            files={uploaded_file.name: bytes_data})
    except ValueError:
        st.error('Please enter a valid input')
    st.write(r)