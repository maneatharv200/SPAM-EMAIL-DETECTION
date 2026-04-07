import streamlit as st
import requests

st.title("📧 Spam Detection Dashboard")

text = st.text_area(
    "Enter Email Text"
)

if st.button("Check Email"):

    url = "http://127.0.0.1:8000/predict"

    response = requests.post(
        url,
        params={"text": text}
    )

    result = response.json()

    st.subheader("Prediction")

    st.write(result["label"])

    st.subheader("Spam Probability")

    st.write(result["spam_probability"])

    st.subheader("Suspicious Links")

    st.write(
        result["links"]
    )

    st.subheader("Explanation")

    st.write(
        result["explanation"]
    )