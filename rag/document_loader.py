from io import BytesIO

from pypdf import PdfReader


def extract_pdf_text(file_bytes):

    reader = PdfReader(
        BytesIO(file_bytes)
    )

    pages = []

    for page in reader.pages:

        text = page.extract_text()

        if text:
            pages.append(text)

    return "\n\n".join(pages)