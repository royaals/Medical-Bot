import streamlit as st
import vertexai
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import VertexAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import VertexAI

# from langchain import PromptTemplate, LLMChain
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from htmlTemplates import css, bot_template, user_template
import requests
from transformers import pipeline
import os
from vertexai.language_models import TextGenerationModel
import pandas as pd

os.environ["GCP_PROJECT"] = "404ERRORNOTFOUND-Niv-Hackathon"


def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text


def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n", chunk_size=2000, chunk_overlap=200, length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks


def get_vectorstore(text_chunks):
    embeddings = VertexAIEmbeddings()
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore


def get_conversation_chain(vectorstore):
    llm = VertexAI()

    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm, retriever=vectorstore.as_retriever(), memory=memory
    )
    return conversation_chain


def handle_userinput(user_question):
    response = st.session_state.conversation({"question": user_question})
    st.session_state.chat_history = response["chat_history"]

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(
                user_template.replace("{{MSG}}", message.content),
                unsafe_allow_html=True,
            )
        else:
            st.write(
                bot_template.replace("{{MSG}}", message.content), unsafe_allow_html=True
            )


def summarize_text(text):
    if len(text) < 30:
        return "Text is too short to summarize"
    parameters = {
        "max_output_tokens": 256,
        "temperature": 0.2,
        "top_p": 0.8,
        "top_k": 40,
    }
    model = TextGenerationModel.from_pretrained("text-bison@001")
    response = model.predict(text, **parameters)
    print(f"Response from Model: {response.text}")
    return response.text


def process_url(url_link):
    response = requests.get(url_link)
    text = response.text
    summarized_text = summarize_text(text)  # Summarize the text
    chunks = get_text_chunks(summarized_text)  # Split the summarized text into chunks
    vectorstore = get_vectorstore(chunks)
    st.session_state.conversation = get_conversation_chain(vectorstore)
    handle_userinput(summarized_text)


m = None


def main():
    load_dotenv()
    st.set_page_config(page_title="Chat")
    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    st.header("chat")
    raw_text = ""
    with st.sidebar:
        st.subheader("Documents Section")
        pdf_docs = st.file_uploader(
            "Ask your Query's here and click on 'Process'", accept_multiple_files=True
        )
        if st.button("Process"):
            with st.spinner("Processing"):
                raw_text = get_pdf_text(pdf_docs)
                chunks = get_text_chunks(raw_text)
                vectorstore = get_vectorstore(chunks)
                st.session_state.conversation = get_conversation_chain(vectorstore)

    if st.session_state and st.session_state.conversation:
        col1, col2 = st.columns([2, 1])

        # Summarized view of the data
        with col1:
            summarized_text = summarize_text(raw_text)
            print(f"[=====] summarized_text: {summarized_text}")

            st.write(summarized_text)

        # Question section
        with col2:
            user_question = st.text_input("Ask a question :")
            if st.button("Submit"):
                handle_userinput(user_question)


if __name__ == "__main__":
    vertexai.init(project="buoyant-road-397110", location="us-central1")
    main()
