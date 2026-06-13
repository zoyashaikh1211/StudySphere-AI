import streamlit as st
from pypdf import PdfReader

# Page Configuration
st.set_page_config(
    page_title="StudySphere AI",
    page_icon="📚",
    layout="wide"
)

# Heading
st.title("📚 StudySphere AI")

st.subheader("Learn Smarter. Revise Faster.")

st.write(
    "Upload your study notes and let AI summarize, explain, quiz, and create flashcards for you."
)

st.divider()

# PDF Upload
uploaded_file = st.file_uploader(
    "📄 Upload your PDF notes",
    type=["pdf"]
)

# Read PDF
if uploaded_file:

    st.success(f"Uploaded: {uploaded_file.name}")

    reader = PdfReader(uploaded_file)

    text = ""

    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted

    st.subheader("📖 Extracted Text Preview")

    st.text_area(
        "PDF Content",
        text[:3000],
        height=300
    )