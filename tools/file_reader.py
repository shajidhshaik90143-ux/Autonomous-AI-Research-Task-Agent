from rag.document_loader import extract_pdf_text


def read_uploaded_pdf(uploaded_file):

    file_bytes = uploaded_file.read()

    return extract_pdf_text(
        file_bytes
    )