from utils.pdf_export import create_pdf
import streamlit as st
from utils.gemini import generate_summary

st.set_page_config(page_title="AI Summary")

st.title("📝 AI Summary")

if "pdf_text" not in st.session_state:
    st.warning("⚠️ Please upload a PDF from the Home page first.")
    st.stop()

text = st.session_state["pdf_text"]

if "summary" not in st.session_state:
    with st.spinner("🤖 Generating Summary..."):
        st.session_state["summary"] = generate_summary(text[:6000])

st.success("✨ Summary Ready!")

st.markdown(st.session_state["summary"])

pdf_file = create_pdf(
    "AI Summary",
    st.session_state["summary"]
)

with open(pdf_file, "rb") as file:

    st.download_button(
        label="📥 Download Summary PDF",
        data=file,
        file_name="StudySphere_Summary.pdf",
        mime="application/pdf"
    )