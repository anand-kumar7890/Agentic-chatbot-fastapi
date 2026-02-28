import streamlit as st
import requests
from dotenv import load_dotenv
load_dotenv()

st.set_page_config(page_title="LangGraph AI Agent", layout="wide")

# ---------------- LOAD CSS ----------------
def load_css():
    with open("static/styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

st.markdown("""
<script>
const panel = window.parent.document.querySelector('.response-panel');
if(panel){
    panel.scrollTop = panel.scrollHeight;
}
</script>
""", unsafe_allow_html=True)

st.title("LangGraph AI Agent")

# ----------- CREATE COLUMNS -------------
left, right = st.columns([1.6, 1])

# ---------------- STATIC RESPONSE SIDE ----------------
left, right = st.columns([1.6, 1])

# -------- LEFT PANEL --------
with left:

    st.markdown('<div class="response-wrapper">', unsafe_allow_html=True)

    if "agent_output" not in st.session_state:
        st.session_state.agent_output = "Response will appear here..."

    response_container = st.empty()

    response_container.markdown(
        f'<div class="response-panel fade-in"><div class="typing">{st.session_state.agent_output}</div></div>',
        unsafe_allow_html=True
    )

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- CONTROL SIDE ----------------
with right:


    st.subheader("Configuration")

    system_prompt = st.text_area("Define your AI Agent:", height=80)

    MODEL_NAMES_GROQ = ["llama-3.3-70b-versatile", "mixtral-8x7b-32768"]
    MODEL_NAMES_OPENAI = ["gpt-4o-mini"]

    provider = st.radio("Select Provider:", ("Groq", "OpenAI"))

    if provider == "Groq":
        selected_model = st.selectbox("Select Groq Model:", MODEL_NAMES_GROQ)
    else:
        selected_model = st.selectbox("Select OpenAI Model:", MODEL_NAMES_OPENAI)

    allow_web_search = st.checkbox("Enable Web Search")

    user_query = st.text_area("Enter your query:", height=150)

    ask_button = st.button("Ask Agent")

    st.markdown('</div>', unsafe_allow_html=True)
    

# ---------------- BACKEND CALL ----------------
API_URL = os.getenv("API_URL")

if ask_button:
    if user_query.strip():

        payload = {
            "model_name": selected_model,
            "model_provider": provider,
            "system_prompt": system_prompt,
            "messages": [user_query],
            "allow_search": allow_web_search
        }

        with st.spinner("Thinking..."):
            response = requests.post(API_URL, json=payload)

        if response.status_code == 200:
            response_data = response.json()

            if "error" in response_data:
                st.session_state.agent_output = response_data["error"]
            else:
                st.session_state.agent_output = response_data

        else:
            st.session_state.agent_output = f"Backend Error: {response.status_code}"

        response_container.markdown(
            f'<div class="response-panel">{st.session_state.agent_output}</div>',
            unsafe_allow_html=True
        )