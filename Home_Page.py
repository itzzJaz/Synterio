import streamlit as st
import time
from document_proccesing import process as pt
from networking import ask_ai
import random
names = [
    "Aarav",
    "Aanya",
    "Aditya",
    "Ananya",
    "Arjun",
    "Diya",
    "Ishaan",
    "Ira",
    "Kabir",
    "Kiara",
    "Krishna",
    "Meera",
    "Neha",
    "Rohan",
    "Riya",
    "Sara",
    "Shiv",
    "Saanvi",
    "Vikram",
    "Zara"
]
Greetings = [
    "Hello",
    "Hi",
    "Hey",
    "Howdy",
    "What’s up",
    "Yo",
    "Hi there",
    "Hey there",
    "Greetings",
    "Salutations",
    "Nice to see you",
    "Long time no see",
    "How are you",
    "How’s it going",
    "Welcome",
    "Hey friend",
    "Good day"
]
st.set_page_config(
    page_title="Synterio",
    page_icon="📘",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.markdown("""
<div style="text-align:center; padding-top:10px; padding-bottom:10px;">
    <h1 style="margin-bottom:5px;">Synterio – Learn Smarter</h1>
    <p style="color:gray; font-size:18px; margin-top:0;">
        Ask questions, and learn step-by-step with AI.
    </p>
</div>
<style>
    .main {
        background-color: #0e1117;
    }

    .stButton>button {
        border-radius: 10px;
        padding: 0.5rem 1rem;
        
        border: 2px solid #F5276C;
        font-weight: 600;
    }

    .stButton>button:hover {
        
        border: 2px solid #d81e5b;
        
    }

    .stTextInput>div>div>input {
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

content = pt(st.file_uploader("Upload your Content"))
question = st.chat_input("Enter Your message")
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
        st.markdown(x)
    with st.spinner('Thinking...'):
        with st.chat_message("Assistant"):
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
                st.markdown(result)
else:
    with st.chat_message("Assistant"):
        st.markdown(f"{random.choice(Greetings)}, I am {random.choice(names)} and I am going to be your tutor today")


