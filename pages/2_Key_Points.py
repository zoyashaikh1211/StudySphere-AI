import streamlit as st
from utils.gemini import generate_keypoints

st.set_page_config(page_title="Key Points")

st.title("💡 AI Key Points")

if "pdf_text" not in st.session_state:
    st.warning("⚠️ Please upload a PDF from the Home page first.")
    st.stop()

text = st.session_state["pdf_text"]

if "keypoints" not in st.session_state:
    with st.spinner("🤖 Extracting Key Points..."):
        st.session_state["keypoints"] = generate_keypoints(text[:6000])

st.success("✨ Key Points Ready!")

st.markdown(st.session_state["keypoints"])