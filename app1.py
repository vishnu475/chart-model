import streamlit as st
from datetime import datetime
import requests
import json
from callollama import callOLLAMA # Assuming this is your module


# Page configuration
st.set_page_config(
    page_title="CHART MODEL",
)

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hello, I am a smart chart model. How can I help you?!"
        }
    ]

if "is_typing" not in st.session_state:
    st.session_state.is_typing = False

# UI Elementsstreamlit run ""
st.title("OFFLINE  CHART") 
st.markdown("Welcome to the offline chart chart model app! Ask me anything.")

st.subheader("chat now")


for message in st.session_state.messages:
    if message["role"] == "user":
        st.info(message["content"])
    else:
        st.success(message["content"])  

if st.session_state.is_typing:
    st.markdown(" Typing..")
    st.warning("Typing.....")

st.markdown("......") 
st.subheader("your message here")

with st.form(key="chat_form" , clear_on_submit= True):
    user_input = st.text_input(
                "Type your message",
                placeholder="Ask me anything.....!"
    )
    send_button=st.form_submit_button("send message",type="primary")

col1,col2 = st.columns([1,1])

with col1:
    clear_button = st.button("clear chat")

if  send_button and user_input.strip():
    st.session_state.messages.append(
        {
            "role":"user",
            "content": user_input.strip()
        }
    )
    st.session_state.is_typing = True
    st.rerun()

if st.session_state.is_typing:
    user_message = st.session_state.messages[-1]["content"]
    bot_response = callOLLAMA(user_message)
    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":bot_response
        
        }
    )
    st.session_state.is_typing = False
    st.rerun()