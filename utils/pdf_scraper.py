import fitz  # PyMuPDF

def extract_pdf_text(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""

    for page in doc:
        text += page.get_text()

    doc.close()
    return text

pdf_file_path = "/Users/ishikaagarwal/JeevaAI/JeevaAI/GTR2024.pdf"
text_output_path = "extracted_thalassemia_text.txt"

pdf_text = extract_pdf_text(pdf_file_path)

with open(text_output_path, "w", encoding="utf-8") as f:
    f.write(pdf_text)

print("PDF text extracted and saved.")
