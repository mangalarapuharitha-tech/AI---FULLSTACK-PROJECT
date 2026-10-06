import ollama
import streamlit as st
if "messages" not in st.session_state:
    st.session_state.messages = []


question = st.chat_input("You:")
st.write("user: ", question)
st.session_state.messages.append(
        {"role": "user",
         "content": question       }
    )
response = ollama.chat(
        model="llama3.2:3b",
        messages=st.session_state.messages
    )
st.session_state.messages.append(
        {"role": "assistant",
         "content":response["message"]["content"]
        }
    )

st.write("AI:",response["message"]["content"])