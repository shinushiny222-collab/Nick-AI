import streamlit as st
from huggingface_hub import InferenceClient

st.set_page_config(
    page_title="Nick AI",
)

st.title("Nick AI")
st.write("Ask me anything!")

client = InferenceClient(
    api_key=st.secrets["HF_TOKEN"]
)

question = st.chat_input("Ask your question...")

if question:

    with st.chat_message("user"):
        st.write(question)

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful AI assistant."
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )

    answer = response.choices[0].message.content

    with st.chat_message("assistant"):
        st.write(answer)
