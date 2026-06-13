import streamlit as st

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

h1{
text-align:center;
color:#5C4B3B;
font-size:58px;
}

h3{
text-align:center;
color:#876B58;
}

.upload{
background:white;
padding:25px;
border-radius:20px;
box-shadow:0px 4px 12px rgba(0,0,0,0.08);
}

.feature{
background:white;
padding:18px;
border-radius:18px;
text-align:center;
box-shadow:0px 4px 12px rgba(0,0,0,0.06);
margin:10px;
}

</style>
""", unsafe_allow_html=True)

st.markdown("# 🌸 StudySphere AI")

st.markdown("### Your Personal AI Study Room")

st.write(
    "<center>Learn Smarter • Revise Faster • Score Better</center>",
    unsafe_allow_html=True
)

st.write("")
st.write("")

st.file_uploader(
    "📄 Upload PDF",
    type=["pdf"]
)

st.write("")
st.write("")

col1,col2,col3=st.columns(3)

with col1:
    st.info("📝 Summary")

with col2:
    st.info("🧠 Flashcards")

with col3:
    st.info("❓ Quiz")

col4,col5,col6=st.columns(3)

with col4:
    st.info("💬 AI Tutor")

with col5:
    st.info("💡 Key Points")

with col6:
    st.info("📅 Planner")

st.write("")
st.write("")

st.markdown(
"""
<center>

🌿 ☕ 📚 ✨ 🌸 🪴 ⭐

</center>
""",
unsafe_allow_html=True
)