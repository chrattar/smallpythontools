import pymupdf  # PyMuPDF

def extract_text_from_pdf(pdf_file):
    try:
        doc = pymupdf.open(pdf_file)
        text = ""
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            text += page.get_text()
        doc.close()
        return text
    except Exception as e:
        print(f"Error extracting text from {pdf_file}: {str(e)}")
        return None

# Example usage:
pdf_file = "siplast.pdf"  # Replace with your PDF file path relative to the script
extracted_text = extract_text_from_pdf(pdf_file)

if extracted_text:
    print("Extracted text:")
    print(extracted_text)
else:
    print("Text extraction failed.")

