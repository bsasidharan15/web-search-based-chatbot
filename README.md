# web-search-based-chatbot
# 🤖 AI Chat Assistant

## 📌 Overview
### 📝 Description
This AI Chat Assistant is designed to provide users with an interactive and intelligent chatbot experience. By leveraging state-of-the-art AI models, it enables seamless conversation while fetching real-time web search results when necessary. The assistant is built using `Streamlit` and `Langchain`, ensuring a responsive and dynamic user interface.
This project is a **Streamlit-based AI Chat Assistant** that integrates `Langchain`, `Ollama`, and `DuckDuckGoSearchRun` to provide a dynamic conversational experience. It is designed to maintain context, perform web searches when necessary, and generate intelligent responses.

---

## 🚀 Features
- 🗣️ **Conversational AI** powered by `Langchain` and `Ollama`
- 🌐 **Web Search Integration** using `DuckDuckGo`
- 🔄 **Maintains Context** across conversations
- 🎛️ **Customizable Model Temperature** for varied response styles
- 🗑️ **Clear Chat History** feature for fresh interactions

---

## 🛠️ Installation & Requirements
To run this chatbot, install the required dependencies using the following commands:

### 1️⃣ Install Dependencies
```bash
pip install streamlit langchain langchain-core langchain-ollama langchain-community duckduckgo-search
```

### 2️⃣ Run the Chatbot
```bash
streamlit run app.py
```

---

## 📜 How I Built It
### 🏗️ Step-by-Step Implementation
#### **1. Setting Up the Environment**
- Started with a Python virtual environment and installed `Streamlit`, `Langchain`, `Ollama`, and `DuckDuckGoSearchRun`.
- Configured `Streamlit` to manage state and user interactions.

#### **2. Defining the Chat Model**
- Used `Langchain` to integrate `Ollama` as the LLM.
- Set up a system prompt to define assistant behavior.

#### **3. Implementing Web Search**
- Created a function using `DuckDuckGoSearchRun` to fetch relevant search results.
- Integrated web search calls dynamically into the chat workflow.

#### **4. Managing Chat Session**
- Used `Streamlit`'s session state to store messages.
- Implemented user input handling and bot response display.

#### **5. UI & User Interaction**
- Designed a `Streamlit` UI with a sidebar for model configuration.
- Added a `clear chat history` button to reset conversations.

---

## 📝 Future Enhancements
- ✨ Support for additional LLM models.
- 🔍 Improved formatting for search results.
- 🗂️ Persistent chat history storage.

---

## 🤝 Contributing
Contributions are welcome! Open issues and pull requests to improve this project.

---

## 📄 License
This project is licensed under the Apache 2.0 License.

Happy coding! 🚀
