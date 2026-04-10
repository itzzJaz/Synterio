import streamlit as st
import time
from document_proccesing import process as pt
from networking import ask_ai
content = pt(st.file_uploader("Upload your Content"))

question = st.chat_input("Enter Your message")
st.title('Synterio – Learn Smarter')
st.caption("Ask questions, and learn step-by-step with AI.")
st.write("Try asking:")
if st.button("Summarize this"):
    question = "Summarize this"

if st.button("Explain like I'm 5"):
    question = "Explain this in simple terms"
if st.button("Quiz Me"):
    question = "Give me some questions on the basis of the content only and make sure it has at least 5 questions and some multiple choice questions too"
if question is not None  :
    x = question.capitalize()
    with st.chat_message("User"):
        st.write(x)
    with st.spinner('Processing...'):
        result = ask_ai(content,question)
        try:
            reply = result["choices"][0]["message"]["content"]

            typed_text = ""
            placeholder = st.empty()

            for char in reply:
                typed_text += char
                placeholder.markdown(typed_text)
                time.sleep(0.005)
        except:
            st.write(result)


