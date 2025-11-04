### Basic AI Agent with Web UI
import streamlit as st
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

# Load AI model from ollama
llm = OllamaLLM(model="mistral") # you can change to llama3 or deepseek-r1 or any other model

#Define AI chat prompt
prompt = PromptTemplate(
    input_variables=["chat_history", "question"],
    template="Previous _conversation: {chat_history}\nUser: {question}\nAI: ")

# function to run ai chat with memory
def run_chain(question):
    #retrieve chat history manually
    chat_history_text = "\n".join([f"{msg.type.capitalize()}: {msg.content}" for msg in chat_history.messages])
    # run the AI response
    response= llm.invoke(prompt.format(chat_history=chat_history_text, question= question))

    #store new user input and AI response in memory
    st.session_state.chat_history.add_user_message(question)
    


#Basic AI Agent with Memory
# from langchain_community.chat_message_histories import ChatMessageHistory
# from langchain_core.prompts import PromptTemplate
# from langchain_ollama import OllamaLLM
# # Load AI model from ollama
# llm = OllamaLLM(model="mistral")

# # initialize the memory
# chat_history = ChatMessageHistory() # stores conversatio history

# #Define AI chat prompt
# prompt = PromptTemplate(
#     input_variables=["chat_history", "question"],
#     template="Previous _conversation: {chat_history}\nUser: {question}\nAI: ")

# # function to run ai chat with memory
# def run_chain(question):
#     #retrieve chat history manually
#     chat_history_text = "\n".join([f"{msg.type.capitalize()}: {msg.content}" for msg in chat_history.messages])
#     # run the AI response
#     response= llm.invoke(prompt.format(chat_history=chat_history_text, question= question))

#     # Save the conversation to memory
#     chat_history.add_user_message(question)
#     chat_history.add_ai_message(response)

#     return response

# # interractive cli chatbot
# print("\n🤖 AI chatbot with Memory")
# print("Type 'exit' to stop.")

# while True:
#     user_input= input("\n📝 You: ")
#     if user_input.lower() == 'exit':
#         print("\n👋 Goodbye")
#         break
#     ai_response = run_chain(user_input)
#     print(f"\n🤖 AI: {ai_response}")


# Basic AI Agent
# while True:
#     question = input("Your question (or type 'exit' to stop) ):")
#     if question.lower() == 'exit':
#         print('Goodbye!')
#         break
#     response = llm.invoke(question)
#     print("\n AI Response: ", response)