import os

import streamlit as st

from dotenv import load_dotenv


load_dotenv()


st.set_page_config(
    page_title="Settings",
    page_icon="⚙️",
    layout="wide"
)

st.title("⚙️ Settings")

st.subheader("AI Configuration")

model = os.getenv(
    "GROQ_MODEL",
    "groq/compound"
)

st.write(
    f"**Current AI Model:** `{model}`"
)

st.info(
    "The project uses Groq Compound for autonomous "
    "research and built-in web search."
)

st.subheader("🔐 API Key")

api_key = os.getenv(
    "GROQ_API_KEY"
)

if api_key:

    st.success(
        "Groq API key detected."
    )

    st.code(
        "GROQ_API_KEY=********"
    )

else:

    st.error(
        "Groq API key not found."
    )

st.subheader("📁 Project Configuration")

st.write(
    "**Database:** SQLite"
)

st.write(
    "**RAG:** TF-IDF document retrieval"
)

st.write(
    "**UI:** Streamlit"
)

st.write(
    "**Reports:** PDF"
)