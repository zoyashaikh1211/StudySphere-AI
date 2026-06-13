import streamlit as st

st.set_page_config(
    page_title="StudySphere AI",
    page_icon="📚",
    layout="wide"
)

# -------- CSS --------

st.markdown("""
<style>

.stApp{
background-color:#F8F3ED;
}

h1{
color:#5A4634;
text-align:center;
font-size:55px;
}

h3{
text-align:center;
color:#7B6651;
}

p{
text-align:center;
color:#6D5B4A;
}

.stButton>button{
background:#A67B5B;
color:white;
border-radius:12px;
padding:12px 25px;
border:none;
font-size:18px;
}

.stFileUploader{
background:white;
padding:20px;
border-radius:20px;
}

</style>
""",unsafe_allow_html=True)

st.markdown("# 📚 StudySphere AI")

st.markdown("### Learn Smarter. Revise Faster.")

st.markdown(
"""
Upload your notes and let AI create
summaries, flashcards, quizzes and
your own AI tutor.
"""
)

st.write("")

st.file_uploader(
"📄 Upload your PDF",
type=["pdf"]
)

st.write("")
st.write("")

st.markdown(
"""
<center>

🌸 ✨ ☕ 📖 🌿 ⭐ 🪴 💡 🌸

</center>

""",
unsafe_allow_html=True
)