import streamlit as st
from parsers import translate_nl_to_map_data
from display import display_data
from config import DatasetNotFoundError

def main():
    st.set_page_config(layout="centered", page_title="Chat Assistant")
    st.title("Chat Assistant")
    st.write("Hello! :wave: I'm here to chat with you. Ask me anything below!")

    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = ""

    chat = st.text_area(label="Your question here:", placeholder="Ask me anything...")

    if st.button("Send"):
        try:
            data = translate_nl_to_map_data(chat)
        except DatasetNotFoundError as e:
            print(f"Error: {e}")
            st.error("No available dataset could be mapped from the contents of the message.")
            return
        
        display_data(data)

if __name__ == "__main__":
    main()
