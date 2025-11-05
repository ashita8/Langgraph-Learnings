import streamlit as st
from backend import chatbot, retrieve_all_threads
from langchain_core.messages import HumanMessage
import uuid
#******************************************Utilities******************************

# CONFIG = {'configurable': {'thread_id': 'thread-1'}}

def generate_thread_id():
    thred_id = uuid.uuid4()
    return thred_id

def reset_chat():
    thread_id = generate_thread_id()
    st.session_state["thread_id"] = thread_id
    add_threads(st.session_state["thread_id"])
    st.session_state["message_history"] = []

def add_threads(thread_id):
    if thread_id not in st.session_state["all_threads"]:
         st.session_state["all_threads"].append(thread_id)

def load_conversation(thread_id):
    return chatbot.get_state(config={'configurable': {'thread_id': thread_id}}).values['messages']

#*****************************************Session State***************************
# st.session_state -> dict -> 
if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

if "thread_id" not in st.session_state:
    st.session_state["thread_id"] = generate_thread_id()

if "all_threads" not in st.session_state:
    st.session_state["all_threads"] = retrieve_all_threads()

add_threads(st.session_state["thread_id"])

#*********************************************Side Bar*****************************
st.sidebar.title("ASH Chatbot")

if st.sidebar.button("New Chat"):
    reset_chat()

st.sidebar.header("Chat History")

for thread_id in st.session_state["all_threads"][::-1]:
    if st.sidebar.button(str(thread_id)):
        st.session_state["thread_id"] = thread_id
        messages = load_conversation(thread_id)
        tmp_message = []

        for msg in messages:
            if isinstance(msg,HumanMessage):
                role = 'user'
            else:
                role = 'assistant'

            tmp_message.append({'role': role, 'content':msg.content})

        st.session_state["message_history"] = tmp_message

#******************************************Main UI**********************************
# loading the conversation history
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])

#{'role': 'user', 'content': 'Hi'}
#{'role': 'assistant', 'content': 'Hi=ello'}

user_input = st.chat_input('Type here')

if user_input:

    # first add the message to message_history
    st.session_state['message_history'].append({'role': 'user', 'content': user_input})
    with st.chat_message('user'):
        st.text(user_input)

    # first add the message to message_history
    #
    with st.chat_message('assistant'):
        ai_message = st.write_stream(
            message_chunk.content for message_chunk, metadata in chatbot.stream(
                {'messages': [HumanMessage(content=user_input)]}, 
                        config={'configurable': {'thread_id': st.session_state["thread_id"]}},
                        stream_mode = 'messages'
                )
        )
    st.session_state['message_history'].append({'role': 'assistant', 'content': ai_message})