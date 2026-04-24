import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
client = Groq(api_key="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")

st.set_page_config(page_title="Dictionary Helper", page_icon="📘")

st.title("📘 Dictionary/Vocabulary Helper")
st.write("Enter any word to get meaning, synonyms, antonyms, and examples.")

def get_initial_message():
    return [
        {
            "role": "system",
            "content": """
You are a Dictionary and Vocabulary Helper AI.

Format response like this:

Meaning:
Synonyms:
Antonyms:
Example:
"""
        }
    ]

def get_response(messages):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages
    )
    return response.choices[0].message.content

if "messages" not in st.session_state:
    st.session_state.messages = get_initial_message()

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("Enter a word:")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.spinner("Thinking..."):
        reply = get_response(st.session_state.messages)

    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.session_state.history.append((user_input, reply))

for user, bot in reversed(st.session_state.history):
    st.markdown(f"**🧑 You:** {user}")
    st.markdown(f"**📘 AI:** {bot}")
    st.markdown("---")
