import streamlit as st
import requests
import json

st.write("# Cosine similarity between two English-Vietnamese sentences")

eng_sent = st.text_input("Enter an English sentence:")
vie_sent = st.text_input("Enter a Vietnamese sentence:")

inputs = {"eng_sent": eng_sent, "vie_sent": vie_sent}

if st.button("Calculate"):
    result = requests.post(url = "http://0.0.0.0:8000/calculate", data = json.dumps(inputs))

    st.write("Cosine similarity is " + result.text)