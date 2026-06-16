import streamlit as st
from utils.gemini import generate_summary

st.set_page_config(page_title="AI Summary")

st.title("📝 AI Summary")

# Check if PDF exists
if "pdf_text" not in st.session_state:
    st.warning("⚠️ Please upload a PDF from the Home page first.")
    st.stop()

text = st.session_state["pdf_text"]

# Generate summary only once
if "summary" not in st.session_state:

    with st.spinner("🤖 Generating AI Summary..."):
        st.session_state["summary"] = generate_summary(text[:6000])

st.success("✨ Summary generated!")

st.markdown(st.session_state["summary"])