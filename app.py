import streamlit as st
from pypdf import PdfReader

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="StudySphere AI",
    page_icon="📚",
    layout="wide"
)

# ---------------- CSS ---------------- #

st.markdown(
    """
    <style>

    .stApp{
        background-color:#F8F3ED;
    }

    h1{
        text-align:center;
        color:#5C4B3B;
        font-size:58px;
    }

    h3{
        text-align:center;
        color:#876B58;
    }

    [data-testid="stFileUploader"]{
        background:white;
        padding:20px;
        border-radius:18px;
        border:1px solid #E7DED3;
    }

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
    }

    .stButton>button:hover{
        background:#EFE6DC;
    }

    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------- HERO ---------------- #

st.markdown(
    """
    <div style="text-align:center;
    padding:25px;
    background:white;
    border-radius:25px;
    box-shadow:0px 4px 15px rgba(0,0,0,0.08);
    margin-bottom:20px;">

    <h1 style="color:#5C4B3B;font-size:60px;margin-bottom:0;">
    🌸 StudySphere AI
    </h1>

    <h3 style="color:#876B58;">
    Your Personal AI Study Room
    </h3>

    <p style="color:#9A806A;font-size:18px;">
    Learn Smarter • Revise Faster • Score Better
    </p>

    </div>
    """,
    unsafe_allow_html=True,
)

st.success(
    """
✨ AI can instantly generate:

📝 Summary

💡 Key Points

🧠 Flashcards

❓ Quiz

💬 AI Tutor

📅 Study Planner
"""
)

# ---------------- FILE UPLOAD ---------------- #

st.subheader("📄 Upload your Study Notes")

uploaded_file = st.file_uploader(
    "Choose your PDF",
    type=["pdf"]
)

# ---------------- PDF ---------------- #

if uploaded_file is not None:

    reader = PdfReader(uploaded_file)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text

    st.session_state["pdf_text"] = text

    words = len(text.split())
    pages = len(reader.pages)
    minutes = max(1, words // 200)

    st.success("✅ PDF Loaded Successfully!")

    c1, c2, c3 = st.columns(3)

    c1.metric("📄 Pages", pages)
    c2.metric("📝 Words", words)
    c3.metric("⏱ Reading Time", f"{minutes} min")

st.divider()

# ---------------- BUTTONS ---------------- #

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

# ---------------- FOOTER ---------------- #

st.divider()

st.markdown(
    """
    <center>

    <h4 style="color:#876B58;">
    🌸 StudySphere AI
    </h4>

    <p>
    Made with ❤️ using Streamlit + Gemini AI
    </p>

    </center>
    """,
    unsafe_allow_html=True,
)

