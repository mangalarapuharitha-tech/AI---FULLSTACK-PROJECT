import ollama
import streamlit as st
st.title(":blue[***My ChatBot App 💬***]")
with st.sidebar:
    personalities = {
        "kid 👧": "You are a kid, you are very curious and playful. Give me answer in 3 lines only.",
        "Professor 👩‍🎓": "Your a IIT Professor, Explain the topic uing corrunt technology. Give me answer in 10 lines only.",
        "Student 👩‍🏫": "You are a student, you are very curious and playful. Give me answer in 5 lines only."
    }
    personality = st.selectbox("Select Personality", personalities.keys())
    if st.button("Clear Chat "):
        st.session_state.messages=[]
        st.success("Chat cleared successfully... 😊 ")
    st.header("Chat Settings ")
    uploaded_file = st.file_uploader("upload a file... ^_^ ")
    if uploaded_file:
        st.write("file uploaded successfully...")
        with st.expander("Preview"):
            context = uploaded_file.read().decode("utf-8")
            st.text(context)
if "messages" not in st.session_state:
    st.session_state.messages=[]
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
question =st.chat_input("you:")
if question:
    with st.chat_message("user"):
        st.write("user: ",question)

st.session_state.messages.append(
    {"role":"user",
    "content":question}
)
with st.spinner("thinking...."):
    response =ollama.chat(
            model="llama3.2:3b",
            messages=[{
                "role":"system", "content":personalities[personality]
            }] + st.session_state.messages
        )
st.session_state.messages.append(
        {"role":"assistant",
         "content":response["message"]["content"]
        }
    )
with st.chat_message("assistant"):
    st.write("AI:",response["message"]["content"])