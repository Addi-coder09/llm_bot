import streamlit as st
import requests

# Page config
st.set_page_config(
    page_title="LLM Chatbot",
    page_icon="🧠",
    layout="centered"
)

# Stylish header and styling
st.markdown("""
    <style>
        .main-title {
            font-size: 38px;
            font-weight: bold;
            color: #3C5A99;
            text-align: center;
            margin-bottom: 0px;
        }
        .subtitle {
            font-size: 18px;
            color: #888;
            text-align: center;
            margin-top: 0px;
            margin-bottom: 30px;
        }
        .chat-bubble-user {
            background-color: #DCF8C6;
            color: black;
            padding: 10px;
            border-radius: 10px;
            margin-bottom: 5px;
            max-width: 80%;
        }
       .chat-bubble-bot {
         background-color: #F1F0F0;
         color: black; 
         padding: 10px;
         border-radius: 10px;
         margin-bottom: 20px;
    max-width: 80%;
}

        .credit {
            font-size: 14px;
            text-align: center;
            color: #777;
            margin-top: 50px;
        }
        .stTextInput > div > div > input {
            font-size: 16px;
            padding: 10px;
        }
        button[kind="primary"] {
            background-color: #3C5A99 !important;
            color: white !important;
        }
    </style>
""", unsafe_allow_html=True)

# Heading and subtitle
st.markdown('<div class="main-title">💬 Local LLM Chatbot</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Created for Arch Technologies by Abdul Rehman Malik</div>', unsafe_allow_html=True)

# Session state for history
if "history" not in st.session_state:
    st.session_state.history = []

# Input field
user_input = st.text_input("Type your message here:")

# Function to call Ollama
def ask_ollama(prompt):
    url = "http://localhost:11434/api/generate"
    data = {
        "model": "llama2",
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(url, json=data)
    return response.json()["response"]

# Show chat bubbles
for q, a in st.session_state.history:
    st.markdown(f'<div class="chat-bubble-user"><b>You:</b> {q}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="chat-bubble-bot"><b>Bot:</b> {a}</div>', unsafe_allow_html=True)

# ✅ BUG-FREE: Process input once only
if user_input and "last_input" not in st.session_state:
    response = ask_ollama(user_input)
    st.session_state.history.append((user_input, response))
    st.session_state.last_input = user_input
    st.rerun()

# Clear last_input after rerun
if "last_input" in st.session_state:
    del st.session_state["last_input"]

# Reset Chat
if st.button("🔁 Reset Chat"):
    st.session_state.history = []
    st.rerun()

# Footer
st.markdown('<div class="credit">Powered by Ollama & Streamlit</div>', unsafe_allow_html=True)
