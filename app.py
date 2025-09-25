import streamlit as st
from transformers import pipeline

# Load a pretrained model (replace with your fine-tuned one if available)
qa_model = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

st.title("💊 Medical Chatbot | Generative AI")
st.write("Ask a medical question and get AI-powered answers.")

question = st.text_input("Enter your medical question:")

if question:
    context = "This is a general medical knowledge base. Always consult a doctor for serious conditions."
    result = qa_model(question=question, context=context)
    st.write("**Answer:**", result["answer"])
