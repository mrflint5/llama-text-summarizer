# frontend/app.py
import streamlit as st
import requests

st.title("LLaMA Text Summarizer")

user_input = st.text_area("Enter text to summarize", height=250)
model = st.text_input("Model name (optional)", value="llama2")

if st.button("Summarize") and user_input.strip():
    with st.spinner("Generating summary..."):
        try:
            resp = requests.post("http://localhost:8000/summarize", json={"text": user_input, "model": model}, timeout=60)
            resp.raise_for_status()
            summary = resp.json().get("summary", "No summary returned.")
            st.subheader("Summary")
            st.write(summary)
        except Exception as e:
            st.error(f"Error: {e}")
