from pypdf import PdfReader
import re
def pdf_reading(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""

    for page in reader.pages:  # Fixed typo (was "pages", should be "page")
        extracted_text = page.extract_text()  # Correct reference
        if extracted_text:
            text += extracted_text + "\n"

    return text.strip()  # Fixed the incorrect `.st`

def clean_resume_text(text):
    """Cleans extracted text by removing special characters and extra spaces"""
    text = re.sub(r'\s+', ' ', text)  # Remove multiple spaces/newlines
    text = re.sub(r'[^\w\s@.-]', '', text)  # Keep letters, numbers, emails, etc.
    return text.strip()

