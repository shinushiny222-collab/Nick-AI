import os
import streamlit as st
from huggingface_hub import InferenceClient

st.set_page_config(
    page_title="AI Chatbot",
)

st.title("Hugging Face AI Chatbot")
st.write("Ask me anything!")

client = InferenceClient(
    api_key=os.environ["HF_TOKEN"]
)

question = st.text_input("Enter your question:")

if st.button("Generate"):
    if question:
        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {
                    "role": "user",
                    "content": question
                }
            ]
        )

        answer = response.choices[0].message.content

        st.success("AI Response")
        st.write(answer)

    else:
        st.warning("Please enter a question.")