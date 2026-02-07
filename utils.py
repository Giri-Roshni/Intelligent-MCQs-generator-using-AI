import pdfplumber

def read_syllabus(uploaded_file):
    text = ""
    if uploaded_file.type == "application/pdf":
        with pdfplumber.open(uploaded_file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    else:
        # For TXT files
        text = uploaded_file.read().decode("utf-8")
    return text
