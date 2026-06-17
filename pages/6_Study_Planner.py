import streamlit as st
from utils.gemini import generate_planner

st.set_page_config(page_title="Study Planner")

st.title("📅 AI Study Planner")

if "pdf_text" not in st.session_state:
    st.warning("⚠️ Please upload a PDF from the Home page first.")
    st.stop()

text = st.session_state["pdf_text"]

if "planner" not in st.session_state:

    with st.spinner("🤖 Creating your Study Plan..."):

        st.session_state["planner"] = generate_planner(text[:6000])

st.success("✨ Study Plan Ready!")

st.markdown(st.session_state["planner"])

