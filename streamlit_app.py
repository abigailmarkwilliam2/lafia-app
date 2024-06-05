## Conversational Q&A Chatbot with session knowledge
import streamlit as st
import os

model = ChatGoogleGenerativeAI(model="gemini-pro", convert_system_message_to_human=True)


st.set_page_config(page_title="Q&A Demo")

st.header("Gemini LLM Application")

if 'flowmessages' not in st.session_state:
    st.session_state['flowmessages']=[
        SystemMessage(content="you are a helpfull AI assistant")
    ]

def get_gemini_response(question):

    st.session_state['flowmessages'].append(HumanMessage(content=question))
    response=model.invoke(st.session_state['flowmessages'])
    st.session_state['flowmessages'].append(AIMessage(content=response.content))    
    return response

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []


input=st.text_input("Input: ",key="input")
#response=get_gemini_response(input)

submit=st.button("Ask the question")


if submit and input:
    response=get_gemini_response(input)
    st.session_state['chat_history'].append(("You", input))
    st.subheader("The Response is")
    st.write(response.content)
    st.session_state['chat_history'].append(("Bot", response.content))

st.subheader("The Chat History is")
    
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")
    
