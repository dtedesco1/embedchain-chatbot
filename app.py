# Chatbot

import os
import streamlit as st

def main():
    openai_api_key = st.text_input("Enter your OpenAI API key:", type="password")

    if openai_api_key:
        os.environ["OPENAI_API_KEY"] = openai_api_key
        st.write("API key set successfully!")
    else:
        st.error("Please enter your API key.")

    text_input = st.text_input("Enter your reference text here:")

    if text_input:
        try:
            st.title("Talk to your text")

            from embedchain import App

            chat_bot = App()

            chat_bot.add_local('text', text_input)

            user_query = st.text_input("Enter your question:")

            if st.button("submit"):
                try:
                    result = chat_bot.query(user_query)
                    st.write(result)
                except Exception as e:
                    st.error(f"An error occured: {e}")

        except Exception as e:
            st.error(f"An error occured: {e}")

if __name__ == "__main__":
    main()