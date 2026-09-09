import os
import streamlit as st
from huggingface_hub import InferenceClient
st.set_page_config(
    page_title="Nick AI",
    layout="centered"
)
HF_TOKEN = os.getenv("HF_TOKEN")
if not HF_TOKEN:
    try:
        HF_TOKEN = st.secrets["HF_TOKEN"]
    except Exception:
        HF_TOKEN = None
if not HF_TOKEN:
    st.error("Hugging Face API token is not configured.")
    st.info(
        "For Streamlit Cloud: Go to Manage app → Settings → Secrets "
        "and add HF_TOKEN."
    )
    st.stop()
client = InferenceClient(
    api_key=HF_TOKEN
)

st.title(" Nick AI")
st.caption("Powered by Hugging Face")

st.write("Ask me anything!")


if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])


question = st.chat_input("Type your question...")

if question:

    with st.chat_message("user"):
        st.write(question)

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    try:

        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are Nick AI, a friendly and helpful AI assistant. "
                        "Give clear, simple and useful answers."
                    )
                }
            ] + st.session_state.messages
        )

        answer = response.choices[0].message.content
        with st.chat_message("assistant"):
            st.write(answer)


        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

    except Exception as e:

        st.error("Something went wrong while contacting Hugging Face.")

        st.write("Error:", str(e))