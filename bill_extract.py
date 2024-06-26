import fitz  # PyMuPDF
import re

def extract_text_from_pdf(pdf_file):
    try:
        doc = fitz.open(pdf_file)
        text = ""
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            text += page.get_text()
        doc.close()
        return text
    except Exception as e:
        print(f"Error extracting text from {pdf_file}: {str(e)}")
        return None

def parse_text(text):
    # Define regular expressions for key-value pairs
    patterns = {
        'Order Date': r'Order Date:\s*(\S+)',
        'Order No': r'Order No:\s*(\S+)',
        'Order Amount': r'Order Amount:\s*\$([\d,]+\.\d{2})',
        'Revised On': r'Revised On:\s*(\S+)',
        'Arrival': r'Arrival:\s*(\S+)',
        'Customer PO': r'Customer PO:\s*(\S+)',
        'Weight': r'Weight :\s*([\d,]+\.\d{2})',
        'Date Shipped': r'Date Shipped:\s*(\S+)',
        'Status': r'Status:\s*(\S+)'
    }

    extracted_data = {}

    for key, pattern in patterns.items():
        match = re.search(pattern, text)
        if match:
            extracted_data[key] = match.group(1)

    return extracted_data

# Example usage:
pdf_file = "siplast.pdf"
extracted_text = extract_text_from_pdf(pdf_file)

if extracted_text:
    print("Extracted text:")
    print(extracted_text)
    parsed_data = parse_text(extracted_text)
    print("\nParsed Data:")
    for key, value in parsed_data.items():
        print(f"{key}: {value}")
else:
    print("Text extraction failed.")
