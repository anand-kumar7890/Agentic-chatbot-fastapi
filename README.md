# 🤖 LangGraph AI Agent (Full-Stack AI Application)

A full-stack AI Agent built using FastAPI, Streamlit, LangGraph, Groq, OpenAI, and Tavily Search.

This application allows users to configure and interact with dynamic AI agents through a modern web interface with optional web search capabilities.

---

## 🚀 Features

- Dynamic Model Selection (Groq / OpenAI)
- Custom System Prompt Configuration
- Optional Web Search (Tavily Integration)
- Sticky Glassmorphism UI
- Auto-Scrolling Response Panel
- Typing Animation Effect
- Secure Environment Variable Handling
- Free Deployment Ready (Render)

---

## 🏗 Tech Stack

### Backend
- FastAPI
- LangGraph
- LangChain
- Groq API
- OpenAI API
- Tavily Search API
- Uvicorn

### Frontend
- Streamlit
- Custom CSS (Glassmorphism UI)
- Requests

---

## 📁 Project Structure

    agentic-chatbot/
    │
    ├── backend/
    │ ├── backend.py
    │ ├── ai_agent.py
    │ ├── requirements.txt
    │
    ├── frontend/
    │ ├── frontend.py
    │ ├── static/
    │ │ └── styles.css
    │ ├── requirements.txt
    │
    └── README.md


---

## 🔐 Environment Variables

Create a `.env` file inside the backend directory:
GROQ_API_KEY=your_groq_key
OPENAI_API_KEY=your_openai_key
TAVILY_API_KEY=your_tavily_key


⚠️ Never push `.env` to GitHub.

---

## 🛠 Local Setup

### 1️⃣ Clone Repository
git clone https://github.com/your-username/your-repo.git

cd agentic-chatbot

---

### 2️⃣ Setup Backend
cd backend
pip install -r requirements.txt
uvicorn backend:app --reload --port 9999


Backend runs at: http://127.0.0.1:9999
Swagger Docs: http://127.0.0.1:9999/docs


---

### 3️⃣ Setup Frontend

Open a new terminal:
cd frontend
pip install -r requirements.txt
streamlit run frontend.py
Frontend runs at: http://localhost:8501


Future Improvements

- Streaming responses
- Conversation memory
- Chat history persistence
- Token usage tracking
- Docker containerization
- CI/CD pipeline

---

## 📄 License

This project is open-source under the MIT License.
