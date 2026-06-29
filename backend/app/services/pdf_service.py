import fitz


def extract_pdf_text(filepath: str) -> str:

    document = fitz.open(filepath)

    text = ""

    for page in document:
        text += page.get_text()

    document.close()

    return text