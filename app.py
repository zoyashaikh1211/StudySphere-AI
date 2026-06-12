import streamlit as st

st.set_page_config(
    page_title="StudySphere AI",
    page_icon="📚",
    layout="wide"
)

st.title("📚 StudySphere AI")

st.subheader("Learn Smarter. Revise Faster.")

st.write(
    "Upload your study material and let AI help you summarize, quiz, and chat with your notes."
)

uploaded_file = st.file_uploader(
    "Upload a PDF",
    type=["pdf"]
)