import streamlit as st
from utils.gemini import ask_tutor

st.set_page_config(page_title="AI Tutor")

st.title("💬 AI Tutor")

if "pdf_text" not in st.session_state:
    st.warning("⚠️ Please upload a PDF from the Home page first.")
    st.stop()

text = st.session_state["pdf_text"]

question = st.text_input(
    "Ask anything from your notes..."
)

if st.button("Ask AI"):

    with st.spinner("🤖 Thinking..."):

        answer = ask_tutor(
            text[:6000],
            question
        )

    st.success("✨ Answer")

    st.markdown(answer)

