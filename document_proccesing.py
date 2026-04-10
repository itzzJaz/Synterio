import fitz

def process(uploaded_file):
    if uploaded_file is not  None:
        pdf_bytes = uploaded_file.read()
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text()
        return text
    else:
        return ""