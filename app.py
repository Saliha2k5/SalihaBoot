import streamlit as st
import os
from rag_engine import create_vectorstore, get_answer

st.set_page_config(
    page_title="SalihaBoot - Personal Assistant",
    page_icon="🤖",
    layout="centered"
)

st.markdown("""
    <style>
    .stApp{
background:linear-gradient(135deg,#140021,#240046,#3c096c,#5a189a);
background-size:400% 400%;
animation:gradient 12s ease infinite;
}

@keyframes gradient{

0%{background-position:0% 50%;}

50%{background-position:100% 50%;}

100%{background-position:0% 50%;}

}
    .stChatMessage{
background:rgba(255,255,255,.08)!important;
backdrop-filter:blur(12px);
border:1px solid rgba(255,255,255,.15);
border-radius:18px;
padding:15px;
margin-top:10px;
box-shadow:0 0 15px rgba(0,0,0,.3);
}
    .stChatInputContainer {
        border-top: 2px solid #7b2ff7 !important;
    }
    input { 
        background: #2d1b69 !important;
        color: #e0aaff !important;
        border: 1px solid #c77dff !important;
    }
    .stSpinner { color: #c77dff !important; }
    hr { border-color: #7b2ff7 !important; }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
<h1 class='main-title'>
🤖 SalihaBoot
</h1>

<p style='text-align:center;font-size:20px;'>
Your Personal AI Assistant
</p>
""", unsafe_allow_html=True)
st.divider()
with st.sidebar:

    st.title("🤖 SalihaBoot")

    st.write("---")

    st.write("### Features")

    st.success("AI Chat")

    st.success("RAG Search")

    st.success("Document Assistant")

    st.success("Fast Responses")

    st.write("---")

    st.info("Developed by")

    st.write("❤️ Saliha Ramzan")

CV_PATH = "Saliha_Ramzan_CV.docx"
if CV_PATH is None:
    st.error("❌ No .docx file found! Please add your CV to the folder.")
    st.stop()

if "vectorstore" not in st.session_state:
    with st.spinner("Initializing SalihaBoot..."):
        st.session_state.vectorstore = create_vectorstore(CV_PATH)
        st.success("✅ SalihaBoot is Ready!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask me something about Saliha..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Saliha is Thinking..."):
            answer = get_answer(st.session_state.vectorstore, prompt)
            st.markdown(answer)
            st.session_state.messages.append({
                "role": "assistant",
                "content": answer
            })
            st.divider()

st.markdown(
"""
<center>

Made with ❤️ by <b>Saliha Ramzan</b>

</center>
""",
unsafe_allow_html=True
)