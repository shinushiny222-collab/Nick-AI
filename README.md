# Nick AI – Hugging Face AI Chatbot

Nick AI is an AI-powered chatbot application built using Python, Streamlit, and the Hugging Face Inference API. It provides an interactive chat interface where users can ask questions and receive AI-generated responses.

## Project Overview

Nick AI uses a Hugging Face-hosted Large Language Model to generate intelligent responses to user questions.

The application provides a simple and user-friendly Streamlit interface with chat history support.

### Architecture

```text
User
  |
  v
Streamlit UI
  |
  v
Python Application
  |
  v
Hugging Face InferenceClient
  |
  v
Hugging Face Inference API
  |
  v
openai/gpt-oss-120b
  |
  v
AI Response
  |
  v
Streamlit UI
```

## Features

* AI-powered chatbot
* Interactive chat interface
* Large Language Model integration
* Hugging Face Inference API
* Chat history
* Secure API token handling
* Streamlit web interface
* Streamlit Cloud deployment support
* Simple and user-friendly interface

## Technologies Used

| Technology       | Purpose                         |
| ---------------- | ------------------------------- |
| Python           | Application development         |
| Streamlit        | Web interface                   |
| Hugging Face Hub | AI model inference              |
| InferenceClient  | API communication               |
| GPT Model        | Text generation                 |
| python-dotenv    | Environment variable management |
| GitHub           | Version control                 |
| Streamlit Cloud  | Application deployment          |

## Project Structure

```text
nick-ai/
|
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

```bash
cd nick-ai
```

### 2. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

If `pip` is not recognized, use:

```bash
python -m pip install -r requirements.txt
```

## Hugging Face API Token

Create a Hugging Face account and generate an access token with appropriate permissions.

Never add the actual token directly inside `app.py`.

### Local Environment

In PowerShell:

```powershell
$env:HF_TOKEN="hf_your_token_here"
```

### Streamlit Cloud

Open the Streamlit Cloud application settings:

```text
Manage App
    |
    v
Settings
    |
    v
Secrets
```

Add:

```toml
HF_TOKEN = "hf_your_token_here"
```

## Run the Application

Run the following command from the project directory:

```bash
python -m streamlit run app.py
```

The application will open in the browser.

## Example

### User Input

```text
What is Artificial Intelligence?
```

### AI Response

```text
Artificial Intelligence is a technology that enables computers
to perform tasks that normally require human intelligence.
```

## Deployment

Nick AI can be deployed using Streamlit Community Cloud.

### Deployment Steps

1. Push the project to GitHub.
2. Open Streamlit Community Cloud.
3. Connect the GitHub account.
4. Select the `nick-ai` repository.
5. Select `app.py` as the main file.
6. Add `HF_TOKEN` under Streamlit Secrets.
7. Deploy the application.

## Security

* Never publish the Hugging Face API token.
* Do not commit API tokens to GitHub.
* Do not place API keys directly in source code.
* Use environment variables for local development.
* Use Streamlit Secrets for cloud deployment.

## Future Enhancements

* Voice input
* Text-to-speech
* PDF question answering
* Web search integration
* Multiple AI model selection
* Custom chatbot themes
* User authentication
* Conversation export
* Chat analytics

## Learning Outcomes

Through this project, students can learn:

* Accessing LLMs programmatically
* Hugging Face Hub and Inference API
* API authentication
* Environment variables
* Streamlit application development
* Chat-based UI development
* Secure secret management
* GitHub version control
* Cloud deployment

## Author

**Aseniya Shiny**

B.Sc. Computer Science with Artificial Intelligence

## Demo

https://cfkx4tzcd8ipeebyydvebf.streamlit.app/

## Conclusion

Nick AI demonstrates how a Python application can connect to a Large Language Model through the Hugging Face Inference API and provide an interactive chatbot experience using Streamlit.

The project provides a foundation for developing advanced AI applications such as AI tutors, coding assistants, document assistants, and intelligent customer-support systems.
