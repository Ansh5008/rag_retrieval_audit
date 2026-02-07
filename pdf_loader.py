import os
from pypdf import PdfReader

def load_pdfs(pdf_folder="data/pdfs"):
    documents = []

    for filename in os.listdir(pdf_folder):
        if filename.endswith(".pdf"):
            path = os.path.join(pdf_folder, filename)
            reader = PdfReader(path)

            text = ""
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"

            documents.append({
                "doc_id": filename,
                "text": text.strip()
            })

    return documents
