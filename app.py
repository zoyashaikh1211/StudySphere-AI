import streamlit as st
from pypdf import PdfReader

st.set_page_config(
    page_title="StudySphere AI",
    page_icon="📚",
    layout="wide"
)

st.markdown("""
<style>

.stApp{
    background-color:#F8F3ED;
}

/* Title */

h1{
    text-align:center;
    color:#5C4B3B;
    font-size:58px;
}

h3{
    text-align:center;
    color:#876B58;
}

/* Upload Box */

[data-testid="stFileUploader"]{
    background:white;
    padding:20px;
    border-radius:18px;
    border:1px solid #E7DED3;
}

/* Buttons */

.stButton>button{
    width:100%;
    height:75px;
    border-radius:18px;
    border:none;
    font-size:18px;
    font-weight:bold;
    background:white;
    color:#5C4B3B;
    box-shadow:0px 4px 12px rgba(0,0,0,0.08);
    transition:0.25s;
}

.stButton>button:hover{
    transform:scale(1.03);
    background:#EFE6DC;
}

/* Success Box */

.stAlert{
    border-radius:15px;
}

</style>
""", unsafe_allow_html=True)

st.markdown("# 🌸 StudySphere AI")

st.markdown("### Your Personal AI Study Room")

st.markdown(
"""
<center>

Learn Smarter • Revise Faster • Score Better

</center>
""",
unsafe_allow_html=True
)

st.divider()

st.info("""
📚 Upload your notes once and let AI generate:

• 📝 Summary

• 💡 Key Points

• 🧠 Flashcards

• ❓ Quiz

• 💬 AI Tutor

• 📅 Study Planner
""")

uploaded_file = st.file_uploader(
    "📄 Upload PDF",
    type=["pdf"]
)

if uploaded_file:

    reader = PdfReader(uploaded_file)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text

    st.session_state["pdf_text"] = text

    st.success("✅ PDF loaded successfully!")

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📝 Summary", use_container_width=True):
        st.switch_page("pages/1_Summary.py")

with col2:
    if st.button("🧠 Flashcards", use_container_width=True):
        st.switch_page("pages/3_Flashcards.py")

with col3:
    if st.button("❓ Quiz", use_container_width=True):
        st.switch_page("pages/4_Quiz.py")

col4, col5, col6 = st.columns(3)

with col4:
    if st.button("💬 AI Tutor", use_container_width=True):
        st.switch_page("pages/5_AI_Tutor.py")

with col5:
    if st.button("💡 Key Points", use_container_width=True):
        st.switch_page("pages/2_Key_Points.py")

with col6:
    if st.button("📅 Planner", use_container_width=True):
        st.switch_page("pages/6_Study_Planner.py")

st.divider()

st.markdown(
"""
<center>

🌿 ☕ 📚 ✨ 🌸 🪴 ⭐

<br>

Made with ❤️ using Streamlit & Gemini AI

</center>
""",
unsafe_allow_html=True
)

