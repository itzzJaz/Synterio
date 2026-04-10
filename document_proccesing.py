import fitz
def process(uploaded_file):
    if uploaded_file is None:
        return ""
    file_type = uploaded_file.type

    if file_type == "application/pdf":
        pdf_bytes = uploaded_file.read()
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")

        text = ""
        for page in doc:
            text += page.get_text()

        return text

    elif file_type == "text/plain":
        return uploaded_file.read().decode("utf-8")

    else:
        return "Unsupported file type"