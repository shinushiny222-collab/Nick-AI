import os
import streamlit as st
from huggingface_hub import InferenceClient

st.set_page_config(
    page_title="AI Chatbot",
)

st.title("Hugging Face AI Chatbot")

client = InferenceClient(
    api_key=os.environ["HF_TOKEN"]
)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

question = st.chat_input("Ask something...")

if question:

    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.write(question)

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=st.session_state.messages
    )

    answer = response.choices[0].message.content

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })

    with st.chat_message("assistant"):
        st.write(answer)