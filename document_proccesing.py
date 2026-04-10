import fitz
def process(name):
    doc = fitz.open(f'{name}.pdf')
    print(doc)
    text=""
    for pages in doc:
        text += pages.get_text()
    return text[:8000]

