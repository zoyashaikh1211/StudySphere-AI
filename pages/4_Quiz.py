import streamlit as st
from utils.gemini import generate_quiz

st.set_page_config(page_title="AI Quiz")

st.title("❓ AI Quiz Generator")

if "pdf_text" not in st.session_state:
    st.warning("⚠️ Please upload a PDF from the Home page first.")
    st.stop()

text = st.session_state["pdf_text"]

if "quiz" not in st.session_state:

    with st.spinner("🤖 Creating Quiz..."):
        st.session_state["quiz"] = generate_quiz(text[:6000])

st.success("🎉 Quiz Ready!")

st.markdown(st.session_state["quiz"])