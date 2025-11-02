import docx, PyPDF2

def get_text_from_docx(file):
    doc = docx.Document(file)
    text = []
    for i in doc.paragraphs:
        text.append(i.text)
    text = '\n'.join(text)
    cl = " ".join(text.split())
    return cl

def get_text_from_txt(file):
    with open(file, 'r') as _file:
        text = _file.read()
    return text

def get_text_from_PDF(file):
    reader = PyPDF2.PdfReader(file)
    text = []
    for page in reader.pages:
        t = page.extract_text()
        text.append(t)
    text = '\n'.join(text)
    cl = " ".join(text.split())
    return cl

def get_text_from_input():
    text = input()
    return text

