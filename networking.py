import streamlit as st
import requests

url = "https://router.huggingface.co/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {st.secrets['HF_API_KEY']}",
    "Content-Type": "application/json"
}

def ask_ai(content, question):
    prev_rep = st.session_state.get("prev_rep", "")

    payload = {
        "model": "meta-llama/Llama-3.1-8B-Instruct",
        "messages": [
            {
                "role": "user",
                "content": f"""
You are an AI tutor.

Context:
{content}

Question:
{question}

Your Previous Reply if any:
{prev_rep}
You are a patient tutor. Your goal is to help the student learn, not just get answers. Always explain step-by-step in a clear and structured way. Break down complex ideas into simple parts. Ask guiding questions when helpful. Do not give final answers directly unless the student asks for them. Use simple language and ensure the explanation is easy to understand. If your previous reply included questions provide them with their marking and explain why some questions they got wrong if any and if the user asks to explain a question explain tht question only. If your previous reply was not anywhere near related to the content then know its an error and u may bypass it.If content is none notify the user and try to make sense of what the content could be based on what the user says

"""
            }
        ],
        "temperature": 0.4
    }

    response = requests.post(url, headers=headers, json=payload)
    reply = response.json()["choices"][0]["message"]["content"]
    st.session_state.prev_rep = reply

    return {
        "choices": [
            {"message": {"content": reply}}
        ]
    }