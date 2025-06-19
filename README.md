# RAG Chatbot with Azure Prompt Flow

A simple Streamlit-based web application that provides an AI-powered chatbot interface, leveraging Azure PromptFlow RAG (Retrieval-Augmented Generation) endpoints.

## Features

- Interactive chat interface powered by Streamlit
- Connects to Azure PromptFlow RAG endpoint for intelligent responses
- Maintains chat history within the session
- Easy deployment to Azure Web App via GitHub Actions

## Getting Started

### Prerequisites

- Python 3.13+
- Azure PromptFlow RAG endpoint and API key

### Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/your-username/azure-promptflow-rag-chat.git
   cd azure-promptflow-rag-chat

2. **Create a virtual env:**
   ``` 
   python3 -m venv venv
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**

Copy .env.sample to .env and fill in your Azure PromptFlow RAG details


5. **Run Locally**
Start the Streamlit app:

Visit http://localhost:8000 in your browser.

### Deployment
This project includes a GitHub Actions workflow for deploying to Azure Web App. Refer the configuration file at [.github/workflows/](.github/workflows/)