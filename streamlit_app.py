import streamlit as st
from langchain.llms import Ollama

# Initialize Ollama with model and server
ollama = Ollama(base_url='http://localhost:11434', model='llama3.2:1b')

# Streamlit UI setup
st.set_page_config(page_title="Python Chatbot", layout="wide")

# Title and description
st.title("Python Programming Chatbot 🤖")
st.markdown("I specialize in Python-related questions. Ask me anything about Python programming!")

# Sidebar for chat history
st.sidebar.header("Chat History")
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# Input and process user queries
user_input = st.text_input("Enter your question:")
if st.button("Ask"):
    if user_input.strip():
        try:
            # Python-specific prompt
            prompt = f"""
            You are a chatbot that specializes in Python programming. 
            Only answer questions directly related to Python code, libraries, or programming concepts. 
            If the user's question is unrelated to Python programming, respond strictly with:
            'Sorry, I am only able to answer Python programming-related questions.' 

            User's question: {user_input}
            """
            # Query Ollama model (passing the prompt as a string)
            response = ollama(prompt)

            # Save chat to session state
            st.session_state["chat_history"].append({"user": user_input, "bot": response})
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a valid question.")

# Display chat history in sidebar
for idx, chat in enumerate(st.session_state["chat_history"]):
    with st.sidebar.expander(f"Chat {idx + 1}"):
        st.write(f"**You:** {chat['user']}")
        st.write(f"**Bot:** {chat['bot']}")

# Main chat display
if st.session_state["chat_history"]:
    st.subheader("Chat")
    for chat in st.session_state["chat_history"]:
        st.write(f"**You:** {chat['user']}")
        st.write(f"**Bot:** {chat['bot']}")
