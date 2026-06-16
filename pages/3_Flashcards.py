import streamlit as st
from utils.gemini import generate_flashcards

st.set_page_config(page_title="Flashcards")

st.title("🧠 AI Flashcards")

if "pdf_text" not in st.session_state:
    st.warning("⚠️ Upload a PDF from Home first.")
    st.stop()

text = st.session_state["pdf_text"]

if "flashcards" not in st.session_state:

    with st.spinner("🤖 Creating Flashcards..."):
        st.session_state["flashcards"] = generate_flashcards(text[:6000])

st.success("✨ Flashcards Ready!")

st.markdown(st.session_state["flashcards"])