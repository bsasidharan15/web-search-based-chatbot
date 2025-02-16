import streamlit as st
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_ollama import ChatOllama
from langchain_community.tools import DuckDuckGoSearchRun
import time

# System prompt for the chat assistant
SYSTEM_PROMPT = """You are a helpful chat assistant with the ability to search the web and provide accurate information. You should:
1. Engage in natural conversation
2. Search the web when needed to provide accurate information
3. Maintain context of the conversation
4. Be concise but informative in your responses
5. Acknowledge when you need to search for information"""

class WebSearchTool:
    def __init__(self):
        self.search = DuckDuckGoSearchRun()

    def search(self, query: str):
        try:
            results = self.search.invoke(query)
            return results
        except Exception as e:
            st.error(f"Error fetching search results: {e}")
            return None

def initialize_session_state():
    if 'messages' not in st.session_state:
        st.session_state.messages = [SystemMessage(content=SYSTEM_PROMPT)]
    if 'search_tool' not in st.session_state:
        st.session_state.search_tool = WebSearchTool()
    if 'llm' not in st.session_state:
        st.session_state.llm = ChatOllama(model="mistral-nemo:latest", temperature=0.7)

def display_chat_message(message, is_user: bool):
    avatar = "👤" if is_user else "🤖"
    with st.chat_message(avatar):
        st.write(message.content)
        time.sleep(0.1)

def process_message(user_input: str):
    user_message = HumanMessage(content=user_input)
    st.session_state.messages.append(user_message)
    display_chat_message(user_message, is_user=True)

    search_need_prompt = f"""
    Based on this user message, determine if I need to search the web for information:
    "{user_input}"
    Reply with just 'yes' or 'no'.
    """
    needs_search = st.session_state.llm.invoke(search_need_prompt).content.lower().strip() == 'yes'

    if needs_search:
        with st.spinner("🔍 Searching for information..."):
            search_query = user_input
            results = st.session_state.search_tool.search(search_query)
            if not results:
                response = "I apologize, but I'm having trouble searching for information right now. Let me try to help based on what I know."
            else:
                response = results
    else:
        response = st.session_state.llm.invoke(st.session_state.messages).content

    ai_message = AIMessage(content=response)
    st.session_state.messages.append(ai_message)
    display_chat_message(ai_message, is_user=False)

def create_sidebar():
    with st.sidebar:
        st.title("📱 Chat Settings")
        
        st.subheader("Model Configuration")
        temperature = st.slider("Temperature", 0.0, 1.0, 0.7, 0.1, help="Higher values make responses more creative")
        
        if temperature != st.session_state.llm.temperature:
            st.session_state.llm = ChatOllama(model="mistral-nemo:latest", temperature=temperature)
        
        if st.button("🗑️ Clear Chat History"):
            st.session_state.messages = [SystemMessage(content=SYSTEM_PROMPT)]
            st.rerun()
        
        st.subheader("Chat Statistics")
        message_count = len(st.session_state.messages) - 1
        st.write(f"Messages in conversation: {message_count}")

def main():
    st.set_page_config(page_title="AI Chat Assistant", page_icon="🤖", layout="wide")
    initialize_session_state()
    create_sidebar()
    
    st.title("🤖 AI Chat Assistant")
    st.caption("Ask me anything! I can search the web to help answer your questions.")
    
    for message in st.session_state.messages[1:]:
        display_chat_message(message, is_user=isinstance(message, HumanMessage))
    
    user_input = st.chat_input("Type your message here...")
    if user_input:
        process_message(user_input)

if __name__ == "__main__":
    main()
