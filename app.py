import streamlit as st
import urllib.request
import json

from config import *

st.title("AI Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Get user input
if query := st.chat_input("Enter your message"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.markdown(query)

    # Prepare the API request
    data = {"chat_input": query}
    body = str.encode(json.dumps(data))
    url = AZURE_PROMPT_FLOW_RAG_ENDPOINT
    api_key = AZURE_PROMPT_FLOW_RAG_API_KEY

    if not api_key:
        st.error("API key is required")
    else:
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + api_key,
            'azureml-model-deployment': AZURE_PROMPT_FLOW_RAG_DEPLOYMENT_NAME
        }

        # Show the assistant's response
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            try:
                req = urllib.request.Request(url, body, headers)
                response = urllib.request.urlopen(req)
                result = response.read()
                result_string = result.decode('utf-8')
                result_json = json.loads(result_string)
                
                # Display the response
                assistant_response = result_json["chat_output"]
                message_placeholder.markdown(assistant_response)
                
                # Add assistant response to chat history
                st.session_state.messages.append({"role": "assistant", "content": assistant_response})

            except urllib.error.HTTPError as error:
                message_placeholder.error(f"Request failed with status code: {error.code}\n{error.info()}")
            except Exception as e:
                message_placeholder.error(f"An error occurred: {str(e)}")