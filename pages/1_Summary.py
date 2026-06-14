import streamlit as st

st.set_page_config(page_title="AI Summary")

st.title("📝 AI Summary")

uploaded_file = st.file_uploader(
    "Upload your PDF",
    type=["pdf"]
)

if uploaded_file:
    st.success(f"Uploaded: {uploaded_file.name}")

    st.info("🤖 AI summary will appear here.")