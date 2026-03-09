import streamlit as st
import requests
from dotenv import load_dotenv
import os
from pathlib import Path

load_dotenv()

st.set_page_config(page_title="LangGraph AI Agent", layout="wide")

# ---------------- LOAD CSS ----------------
def load_css():
    css = Path(__file__).parent / "styles.css"
    with open(css) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# auto scroll script
st.markdown("""
<script>
setTimeout(() => {
    const chat = window.parent.document.querySelector('#chat-container');
    if(chat){
        chat.scrollTop = chat.scrollHeight;
    }
}, 200);
</script>
""", unsafe_allow_html=True)

st.title("LangGraph AI Agent")

# ----------- CREATE COLUMNS -------------
left, right = st.columns([1.8, 1])

# -------- LEFT PANEL --------
with left:
    st.markdown("### 🤖 Chat")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    st.markdown('<div id="chat-container" class="chat-container">', unsafe_allow_html=True)

    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(
                f'<div class="user-msg">{msg["content"]}</div>',
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f'<div class="bot-msg">{msg["content"]}</div>',
                unsafe_allow_html=True
            )

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- CONTROL SIDE ----------------
with right:

    st.markdown("### ⚙️ Agent Configuration")

    system_prompt = "You are a helpful AI assistant."

    MODEL_NAMES_GROQ = [
        "llama-3.3-70b-versatile"
    ]

    provider = st.radio("Select Provider:", ("Groq",))

    if provider == "Groq":
        selected_model = st.selectbox("Select Groq Model:", MODEL_NAMES_GROQ)

    allow_web_search = st.checkbox("Enable Web Search")

    user_query = st.text_area(
        "💬 Enter your query",
        height=150,
        placeholder="Ask your AI agent something..."
    )

    ask_button = st.button("🚀 Ask Agent")

# ---------------- BACKEND CALL ----------------
API_URL = os.getenv(
    "API_URL",
    "https://agentic-chatbot-backend.onrender.com/chat"
)

st.write("Using API:", API_URL)

if ask_button and user_query.strip():

    st.session_state.messages.append({
        "role": "user",
        "content": user_query
    })

    payload = {
        "model_name": selected_model,
        "model_provider": provider,
        "system_prompt": system_prompt,
        "messages": [user_query],
        "allow_search": allow_web_search
    }

    with st.spinner("🤖 Agent is thinking..."):
        try:
            response = requests.post(API_URL, json=payload, timeout=120)
        except Exception:
            st.error("Backend connection failed.")
            st.stop()

    if response.status_code == 200:
        response_data = response.json()

        if "error" in response_data:
            agent_reply = response_data["error"]
        else:
            agent_reply = response_data

    else:
        agent_reply = f"Backend Error: {response.status_code}"

    st.session_state.messages.append({
        "role": "assistant",
        "content": agent_reply
    })

    st.rerun()